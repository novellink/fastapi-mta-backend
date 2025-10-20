from fastapi import FastAPI
from app.routers import user_router, auth_router

app = FastAPI(title="Meditouch API", version="1.0.0")

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(auth_router.router, prefix="/mtm", tags=["Mtm"])

@app.get("/")
def root():
    return {"message": "Welcome to Meditouch API"}
