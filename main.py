from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from items import itemsRouter


app = FastAPI(
    debug=True,
    version="0.1.0",
    title="FastAPI test",
    description="This is a test of the FastAPI framework",
    contact={
        "name": "Fabien Bellanger",
        "url": "https://fabien-bellanger.fr",
    },
)


# Middlewares
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])


# Routes
app.include_router(itemsRouter, prefix="/v1")


@app.get("/", name="Home", tags=["Home"])
def read_root():
    return {"Hello": "World"}
