from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    # Rate of 1 unit of this currency expressed in EUR
    rate_to_eur = 1.0
    code = "EUR"

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        rate = cls.rate_to_eur / other_cls.rate_to_eur
        return f"{rate} {other_cls.code} for 1 {cls.code}"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        new_value = self.value * self.rate_to_eur / other_cls.rate_to_eur
        return other_cls(new_value)

    def _value_in_eur(self) -> float:
        return self.value * self.rate_to_eur

    def __str__(self) -> str:
        return f"{self.value} {self.code}"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other: Currency) -> Currency:
        other_value = other.to_currency(self.__class__).value
        return self.__class__(self.value + other_value)

    def __eq__(self, other: Currency) -> bool:
        return self._value_in_eur() == other._value_in_eur()

    def __lt__(self, other: Currency) -> bool:
        return self._value_in_eur() < other._value_in_eur()

    def __gt__(self, other: Currency) -> bool:
        return self._value_in_eur() > other._value_in_eur()

    def __le__(self, other: Currency) -> bool:
        return self._value_in_eur() <= other._value_in_eur()

    def __ge__(self, other: Currency) -> bool:
        return self._value_in_eur() >= other._value_in_eur()

    def __ne__(self, other: Currency) -> bool:
        return self._value_in_eur() != other._value_in_eur()


class Euro(Currency):
    rate_to_eur = 1.0
    code = "EUR"


class Dollar(Currency):
    rate_to_eur = 0.5
    code = "USD"


class Pound(Currency):
    rate_to_eur = 0.01
    code = "GBP"