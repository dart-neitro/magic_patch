from .module1 import func_from_module1
from .module2 import func_from_module2

from datetime import datetime


def main_func():
    val1 = func_from_module1()
    val2 = func_from_module2()
    val3 = datetime.now()
    return val1, val2, val3

