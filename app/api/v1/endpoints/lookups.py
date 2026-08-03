from fastapi import APIRouter
from app.services.lookup_service import LookupService

# Initialize the router for this file
router = APIRouter(prefix="/lookups", tags=["Lookups"])

@router.get("/credit-cards")
def get_credit_cards():
    return LookupService.get_credit_cards()

@router.get("/spending-categories")
def get_spending_categories():
    return LookupService.get_spending_categories()