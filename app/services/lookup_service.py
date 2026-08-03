from app.schemas.lookup import Lookup

class LookupService:

    @staticmethod
    def get_credit_cards() -> list[Lookup]: 
        return [
            {
                "code": "AMEX_GOLD",
                "description": "American Express Gold Card"
            },
            {
                "code": "CHASE_SAPPHIRE",
                "description": "Chase Sapphire Preferred"
            },
            {
                "code": "AMEX_PLATINUM",
                "description": "American Express Platinum Card"
            }
        ]

    @staticmethod
    def get_spending_categories() -> list[Lookup]:
        return [
            {
                "code": "GROC",
                "description": "Groceries"
            },
            {
                "code": "DINE",
                "description": "Dining"
            },
            {
                "code": "TRAV",
                "description": "Travel"
            }
        ]

