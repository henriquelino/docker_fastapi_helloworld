from fastapi import APIRouter
router = APIRouter(prefix='', tags=["Index pages"])


@router.get("/")
def read_root():
    return {"status": "Running"}