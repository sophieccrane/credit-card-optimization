from app.schemas.credit_card import CreditCard
from app.services.lookup_service import LookupService


class CreditCardService:

    @staticmethod
    def get_credit_card_by_code(code: str) -> CreditCard | None:
        """
        Retrieves a credit card by its code.

        :param code: The code of the credit card to retrieve.

        :return: The CreditCard object corresponding to the provided code.
        :rtype: CreditCard | None
        """
        credit_card_map = dict(LookupService.get_credit_card_categories())
        return credit_card_map.get(code, None)

