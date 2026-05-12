from decimal import Decimal, ROUND_DOWN


class MainConfig:
    PRECISION = 2
    QUANTIZE_FORMAT = Decimal('0.' + '0' * PRECISION)
    ROUND = ROUND_DOWN
