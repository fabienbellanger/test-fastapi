from fastapi import APIRouter, status

# Items router
router = APIRouter(
    include_in_schema=False,
)


@router.get("/", name="Home")
def home():
    return {"Hello": "World"}


@router.get("/hello/{name}", name="Hello")
def home(name: str):
    return "Hello, " + name + "!"


@router.get("/health", name="Heath Check", status_code=status.HTTP_204_NO_CONTENT)
def health_check():
    return None
