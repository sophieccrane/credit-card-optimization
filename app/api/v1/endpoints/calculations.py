from fastapi import APIRouter, Query
from app.services.calculation_service import CalculationService

# Initialize the router for this file
router = APIRouter(prefix="/calculations", tags=["Calculations"])

@router.get("/best-credit-card")
def get_optimization(
    category: str = Query(..., description="The category for which to calculate the best credit card."),
    cards: list[str] = Query(..., description="A list of possible credit cards to evaluate."),
):
    """
    Endpoint to calculate the best credit card based on the provided category and list of possible credit cards to use.

    :param category: The category for which to calculate the best credit card.
    :param cards: A list of possible credit cards to use for the calculation.

    :return: The code of the best credit card for the given category.
    :rtype: str
    """
    return CalculationService.calculate_best_card(category, cards)