# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from typing import Union
from loguru import logger


def true_round(number: float, n: int = 0) -> Union[int, float, None]:
    """
    真正意义上的四舍五入到指定的小数位数/True rounding

    :param number: Number to round
    :param n: The number of digits to reserve, the default is 0, which means rounding to an integer
    :return: The result after rounding
    """
    if n < 0:
        logger.error("n must be a non-negative integer")
        return None
    factor = 10 ** n
    rounded_number = int(number * factor + 0.5) / factor

    return rounded_number if n else int(rounded_number)
