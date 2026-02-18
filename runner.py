if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="src.main:main",
        reload=True,
        loop="uvloop",
        port=7000,
        factory=True,
        host="0.0.0.0",
    )
