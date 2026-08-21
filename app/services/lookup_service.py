from app.schemas.lookup import Lookup

class LookupService:

    @staticmethod
    def get_credit_cards() -> list[Lookup]: 
        return [
            {
                "code": "AMEX_GLD",
                "description": "American Express Gold Card"
            },
            {
                "code": "AMEX_PLTNM",
                "description": "American Express Platinum Card"
            },
            {
                "code": "CHASE_FRDM_UNLTD",
                "description": "Chase Freedom Unlimited Card"
            }
        ]

    @staticmethod
    def get_credit_card_categories() -> list[dict]:
        return [
            {
                "code": "AMEX_GLD",
                "categories": [
                    {
                        "code": "DINE",
                        "dealType": "POINTS",
                        "amount": "4",
                        "amountType": "POINT"
                    },
                    {
                        "code": "GROC",
                        "dealType": "POINTS",
                        "amount": "4",
                        "amountType": "POINT"
                    },
                    {
                        "code": "HOTEL",
                        "dealType": "POINTS",
                        "amount": "5",
                        "amountType": "POINT"
                    },
                    {
                        "code": "FLIGHT",
                        "dealType": "POINTS",
                        "amount": "3",
                        "amountType": "POINT"
                    },
                    {
                        "code": "CAR_RENTAL",
                        "dealType": "POINTS",
                        "amount": "2",
                        "amountType": "POINT"
                    },
                    {
                        "code": "OTHER",
                        "dealType": "POINTS",
                        "amount": "1",
                        "amountType": "POINT"
                    }
                ]
            }, 
            {
                "code": "AMEX_PLTNM",
                "categories": [
                    {
                        "code": "FLIGHT",
                        "dealType": "POINTS",
                        "amount": "5",
                        "amountType": "POINT"
                    },
                    {
                        "code": "HOTEL",
                        "dealType": "POINTS",
                        "amount": "5",
                        "amountType": "POINT"
                    },
                    {
                        "code": "OTHER",
                        "dealType": "POINTS",
                        "amount": "1",
                        "amountType": "POINT"
                    }
                ]
            }, 
            {
                "code": "CHASE_FRDM_UNLTD",
                "categories": [
                    {
                        "code": "TRAVEL_PORTAL",
                        "dealType": "CASHBACK",
                        "amount": "5",
                        "amountType": "PERCENT"
                    },
                    {
                        "code": "DINE",
                        "dealType": "CASHBACK",
                        "amount": "3",
                        "amountType": "PERCENT"
                    },
                    {
                        "code": "DRUGSTORE",
                        "dealType": "CASHBACK",
                        "amount": "3",
                        "amountType": "PERCENT"
                    },
                    {
                        "code": "OTHER",
                        "dealType": "CASHBACK",
                        "amount": "1.5",
                        "amountType": "PERCENT"
                    }
                ]
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
                "code": "HOTEL",
                "description": "Hotels"
            },            
            {
                "code": "FLIGHT",
                "description": "Flights"
            },
            {
                "code": "CAR_RENTAL",
                "description": "Car Rental"
            },
            {
                "code": "OTHER",
                "description": "Other"
            }
        ]

