from .module1 import func_from_module1
from .module2 import func_from_module2

from datetime import datetime as datetime_new_name


def main_func():
    val1 = func_from_module1()
    val2 = func_from_module2()
    val3 = datetime_new_name.now()
    return val1, val2, val3

