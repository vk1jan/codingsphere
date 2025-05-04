from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.routes import auth, projects
from app.models.user import User
from app.auth.dependencies import get_current_active_user

app = FastAPI(
    title="FastAPI JWT RBAC API",
    description="A simple API with JWT authentication and RBAC",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(projects.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)