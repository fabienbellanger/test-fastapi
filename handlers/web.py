from fastapi import APIRouter

# Items router
router = APIRouter(
    include_in_schema=False,
)


@router.get("/", name="Home")
def home():
    return {"Hello": "World"}


@router.get("/health", name="Heath Check")
def health_check():
    return "OK"
