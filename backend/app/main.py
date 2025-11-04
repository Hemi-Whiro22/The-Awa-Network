from fastapi import FastAPI

from .config import get_settings

settings = get_settings()

app = FastAPI(title=settings.project_name, debug=settings.debug)


@app.get("/")
def root():
    return {
        "status": "awake",
        "message": f"{settings.project_name} online 🌕",
        "debug": settings.debug,
    }
