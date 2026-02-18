from tortoise import fields, models


class Report(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    data = fields.JSONField()
    status = fields.CharField(max_length=20, default="pending")
    video_path = fields.CharField(max_length=511, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reports"
