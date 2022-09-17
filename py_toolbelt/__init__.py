import py_toolbelt.list_toolbelt as ltb
import py_toolbelt.dict_toolbelt as dtb
import py_toolbelt.other_toolbelt as otb
import py_toolbelt.int_toolbelt as itb
import py_toolbelt.float_toolbelt as ftb
import py_toolbelt.set_toolbelt as stb
import py_toolbelt.tuple_toolbelt as ttb
from forbiddenfruit import curse, reverse
from py_toolbelt.functions_toolbelt import (
    is_type, handle_division, multithread_pool, cache_db, none_safe, iter_safe, empty_safe
)
import inspect

DATA_TYPE_MODULE_MAP = {list: ltb, dict: dtb, int: itb, float: ftb, set: stb, tuple: ttb}

def activate():
    for data_type, module in DATA_TYPE_MODULE_MAP.items():
        for function_name, function in inspect.getmembers(module, inspect.isfunction):
            if not function_name.startswith('__'):
                curse(data_type, function_name, function)

    for data_type in [set, list, str, dict, tuple, int, float, type(None)]:
        curse(data_type, 'is_none', otb.is_none)
        curse(data_type, 'is_not_none', otb.is_not_none)
    
    curse(object, '_s', otb.safe_access)
    curse(type(None), '_s', otb.safe_none_accessor())

def deactivate():
    for data_type, module in DATA_TYPE_MODULE_MAP.items():
        for function_name, function in inspect.getmembers(module, inspect.isfunction):
            if not function_name.startswith('__'):
                reverse(data_type, function_name)

    for data_type in [set, list, str, dict, tuple, int, float, type(None)]:
        reverse(data_type, 'is_none')
        reverse(data_type, 'is_not_none')
    
    reverse(object, '_s')
    reverse(type(None), '_s')
