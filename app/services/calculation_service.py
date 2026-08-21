from app.services.credit_card_service import CreditCardService


class CalculationService:

    @staticmethod
    def calculate_best_card(category: str, cards: list[str]) -> str:
        """
        Calculates the best credit card based on the provided category and list of possible credit cards to use.

        :param category: The category for which to calculate the best credit card.
        :param cards: A list of possible credit cards to use for the calculation.

        :return: The code of the best credit card for the given category.
        :rtype: str
        """
        if not category:
            raise ValueError("category is required")
        if not cards:
            raise ValueError("cards list cannot be empty")

        best_card_code = cards[0]
        best_amount = -1

        for card_code in cards:
            card = CreditCardService.get_credit_card_by_code(card_code)
            if card is None:
                continue

            for category_detail in card.categories:
                if category_detail.get("code") == category:
                    amount = float(category_detail.get("amount", "0"))
                    if amount > best_amount:
                        best_amount = amount
                        best_card_code = card.code

        return best_card_code
