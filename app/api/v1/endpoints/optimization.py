from fastapi import APIRouter
from app.services.lookup_service import LookupService

# Initialize the router for this file
router = APIRouter(prefix="/optimization", tags=["Optimization"])

@router.get("/calculation")
def get_optimization():
   return "found";