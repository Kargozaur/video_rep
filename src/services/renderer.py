import os
import tempfile
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from moviepy import ImageClip, concatenate_videoclips


class VideoRenderer:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data

    def create_frame(self, index: int, value: Any, temp_dir: str) -> str:  # noqa: ANN401
        plt.figure(figsize=(8, 6))
        x = np.arange(index + 1)
        y = self.data["values"][: index + 1]
        plt.plot(x, y, marker="o", color="b", linewidth=2)
        plt.title(self.data.get("title", "Report"))
        plt.ylim(0, max(self.data["value"]) + 10)
        plt.grid(True)

        frame_path = os.path.join(temp_dir, f"frame_{index:03d}.png")
        plt.savefig(frame_path)
        plt.close()
        return frame_path

    async def generate(self) -> str:
        output_dir = "media/reports"
        os.makedirs(output_dir, exist_ok=True)
        final_path = os.path.join(output_dir, f"report_{os.urandom(4).hex()}.mp4")
        with tempfile.TemporaryFile() as tmp:
            frames = []
            values = self.data.get("values", [])
            for i, v in enumerate(values):
                frame_path = self.create_frame(i, v, tmp)
                clip = ImageClip(frame_path).set_duration(1)
                frames.append(clip)
            video = concatenate_videoclips(frames, method="compose")
            video.write_videofile(final_path, fps=24, codec="libx264")
        return final_path
