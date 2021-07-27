from types import ModuleType
from typing import Union, List
from unittest.mock import Mock, patch
from contextlib import contextmanager
from warnings import warn

import sys


@contextmanager
def magic_patch(
        start_module: ModuleType,
        target_object: object,
        mock_object: object,
        search_by_all_names: bool = False
        ) -> None:

    packages = {}
    try:
        if search_by_all_names:
            packages = search_object_by_all_names_in_loaded_packages(target_object)
        else:
            packages = search_object_by_name_in_loaded_packages(target_object)
        setup_object(packages, mock_object)
        yield mock_object
    except Exception as e:
        raise e
    finally:
        setup_object(packages, target_object)


def search_object_by_name_in_loaded_packages(target_object: object, search_by_all_names: bool = False):
    result = dict()
    target_object_name = target_object.__name__
    for name, module in sys.modules.items():
        if getattr(module, target_object_name, None) is target_object:
            result[name] = target_object_name
    return result


def search_object_by_all_names_in_loaded_packages(target_object: object, search_by_all_names: bool = False):
    result = dict()
    # For avoiding RuntimeError: dictionary changed size during iteration
    uploaded_modules = tuple(sys.modules.items())
    for name, module in uploaded_modules:
        for module_object_name, module_object in _get_module_objects_mapping(module):
            if module_object is target_object:
                result[name] = module_object_name

    return result


def _get_module_objects_mapping(module: ModuleType) -> List:
    try:
        # For avoiding RuntimeError: dictionary changed size during iteration
        uploaded_module_objects = tuple(module.__dict__.items())
    except AttributeError as e:
        warn("Module has no __dict__: {}".format(str(e)))
        return
    for module_object_name, module_object in uploaded_module_objects:
        yield module_object_name, module_object


def setup_object(packages, new_object):
    for module_name, target_object_name in packages.items():
        setattr(sys.modules[module_name], target_object_name, new_object)


