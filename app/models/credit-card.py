from __future__ import annotations
 
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional
 
 
class DealType(str, Enum):
    POINTS = "POINTS"
    CASHBACK = "CASHBACK"
 
 
class AmountType(str, Enum):
    POINT = "POINT"
    PERCENT = "PERCENT"
 
 
class CategoryCode(str, Enum):
    """Spending category taxonomy shared across all cards.
 
    Keeping this as one shared enum (rather than letting each card
    define its own category strings) is what keeps the recommendation
    engine's matching logic simple later on.
    """
    DINE = "DINE"
    GROC = "GROC"
    HOTEL = "HOTEL"
    FLIGHT = "FLIGHT"
    CAR_RENTAL = "CAR_RENTAL"
    DRUGSTORE = "DRUGSTORE"
    TRAVEL_PORTAL = "TRAVEL_PORTAL"
    GAS = "GAS"
    OTHER = "OTHER"
 
 
@dataclass
class RewardCategory:
    code: CategoryCode
    deal_type: DealType
    amount: float
    amount_type: AmountType
    # Optional: restricts the rate to a specific booking channel,
    # e.g. "AMEX_TRAVEL" for Platinum's 5x hotel bonus.
    condition: Optional[str] = None
    # Optional: for temporary/expiring bonus offers (e.g. rotating
    # quarterly categories or limited-time partner promos).
    valid_until: Optional[date] = None
 
    def to_dict(self) -> dict:
        d = {
            "code": self.code.value,
            "dealType": self.deal_type.value,
            "amount": str(self.amount),
            "amountType": self.amount_type.value,
        }
        if self.condition is not None:
            d["condition"] = self.condition
        if self.valid_until is not None:
            d["validUntil"] = self.valid_until.isoformat()
        return d
 
    @classmethod
    def from_dict(cls, data: dict) -> "RewardCategory":
        return cls(
            code=CategoryCode(data["code"]),
            deal_type=DealType(data["dealType"]),
            amount=float(data["amount"]),
            amount_type=AmountType(data["amountType"]),
            condition=data.get("condition"),
            valid_until=(
                date.fromisoformat(data["validUntil"])
                if data.get("validUntil")
                else None
            ),
        )
 
 
@dataclass
class CreditCard:
    code: str
    categories: list[RewardCategory] = field(default_factory=list)
 
    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "categories": [c.to_dict() for c in self.categories],
        }
 
    @classmethod
    def from_dict(cls, data: dict) -> "CreditCard":
        return cls(
            code=data["code"],
            categories=[RewardCategory.from_dict(c) for c in data["categories"]],
        )
 
    def best_category(self, code: CategoryCode) -> Optional[RewardCategory]:
        """Return this card's reward for a category, falling back to OTHER."""
        for cat in self.categories:
            if cat.code == code:
                return cat
        for cat in self.categories:
            if cat.code == CategoryCode.OTHER:
                return cat
        return None
 