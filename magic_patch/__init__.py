from types import ModuleType
from typing import Union
from unittest.mock import Mock, patch
from contextlib import contextmanager

import sys


@contextmanager
def magic_patch(
        start_module: ModuleType,
        target_object: object,
        mock_object: object,
        search_by_all_names: bool = False
        ) -> None:

    try:
        packages = search_object_by_name_in_loaded_packages(target_object)
        setup_object(packages, mock_object)
        yield mock_object
    except Exception as e:
        print(e)
    finally:
        setup_object(packages, target_object)


def search_object_by_name_in_loaded_packages(target_object: object):
    result = dict()
    target_object_name = target_object.__name__
    for name, module in sys.modules.items():
        if getattr(module, target_object_name, None) is target_object:
            result[name] = target_object_name
    return result


def setup_object(packages, new_object):
    for module_name, target_object_name in packages.items():
        setattr(sys.modules[module_name], target_object_name, new_object)

