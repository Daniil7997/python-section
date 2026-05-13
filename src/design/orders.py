from abc import ABC, abstractmethod
from dataclasses import dataclass
from operator import itemgetter
import uuid


@dataclass
class Order:
    """There is no need to describe anything here."""


class Discount(ABC):
    def __init__(self, user_uuid: uuid.UUID):
        self.user_uuid = user_uuid
        self.status = False

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass

    @abstractmethod
    def calculate(self, order: Order):
        pass


class FixedDiscount(Discount):
    fixed_discount: int

    def __init__(self, fixed_discount: int, user_uuid: uuid.UUID):
        self.fixed_discount = fixed_discount
        super().__init__(user_uuid)

    def activate(self):
        pass

    def deactivate(self):
        pass

    def calculate(self, order: Order):
        pass


class LoyalityDiscount(Discount):
    loyality_level: int

    def __init__(self, loyality_level: int, user_uuid: uuid.UUID):
        self.loyality_level = loyality_level
        super().__init__(user_uuid)

    def activate(self):
        pass

    def deactivate(self):
        pass

    def calculate(self, order: Order):
        pass


class PercentDiscount(Discount):
    percent_discount: float

    def __init__(self, percent_discount: float, user_uuid: uuid.UUID):
        self.percent_discount = percent_discount
        super().__init__(user_uuid)

    def activate(self):
        pass

    def deactivate(self):
        pass

    def calculate(self, order: Order):
        pass


class FindBestDiscount():
    def compare(self, order: Order, discounts: list[Discount]) -> tuple:
        if not discounts:
            return None
        tmp = {}
        for discount in discounts:
            tmp[discount] = discount.calculate(order)
        res = sorted(tmp.items(), key=itemgetter(1), reverse=True)
        return res[0]
