from decimal import Decimal
import uuid

from src.wallets.config import MainConfig
from src.wallets.currency import Currency
from src.wallets.exceptions import (CurrencyNotSupported,
                                    NegativeValueException)


class Wallet:
    __slots__ = ('user_uuid', 'rub', 'usd')

    def __init__(self,
                 user_uuid: uuid.UUID = None,
                 rub: int | float | str | Decimal = 0,
                 usd: int | float | str | Decimal = 0):
        self.user_uuid = user_uuid
        self.rub: Decimal = rub
        self.usd: Decimal = usd

    def __setattr__(self, name, value):
        if isinstance(value, (Decimal)):
            if value < 0:
                raise NegativeValueException(f"{name} can't be negative")
            value = value.quantize(MainConfig.QUANTIZE_FORMAT,
                                   rounding=MainConfig.ROUND)
        super().__setattr__(name, value)


class WalletService:
    @staticmethod
    def check_balance(wallet: Wallet) -> dict:
        res = {}
        for atr in wallet.__slots__:
            if atr == 'user_uuid':
                continue
            res[atr] = getattr(wallet, atr)
        return res

    @staticmethod
    def change_balance(wallet: Wallet,
                       money: dict[str, int | float | Decimal]) -> None:
        """
        Key - currency.
        Value - quantity.
        Positive currency for deposits, negative currency for withdrawals.
        """
        for key, value in money.items():
            if hasattr(wallet, key):
                cur_value = getattr(wallet, key)
                valid_money = Decimal(str(value)).quantize(
                    MainConfig.QUANTIZE_FORMAT, rounding=MainConfig.ROUND
                    )
                new_value = cur_value + valid_money
                setattr(wallet, key, new_value)
            else:
                raise CurrencyNotSupported(f'Currency {key} not supported')


wal = Wallet()
WalletService.change_balance(wallet=wal,
                             money={Currency.rub: '1000'})
check = WalletService.check_balance(wallet=wal)
print(check)
