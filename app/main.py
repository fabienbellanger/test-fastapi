from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.handlers import items
from app.handlers import web

# Application
app = FastAPI(
    debug=True,
    version="0.1.0",
    title="FastAPI test",
    description="This is a test of the FastAPI framework",
    contact={
        "name": "Fabien Bellanger",
        "url": "https://fabien-bellanger.fr",
    },
    include_in_schema=True,
    docs_url="/docs",
    redoc_url=None,  # Disable ReDoc page
)


# Middlewares
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "0.0.0.0", "testserver"],
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(web.router)
app.include_router(items.router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8086)
