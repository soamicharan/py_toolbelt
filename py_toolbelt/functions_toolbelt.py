from collections.abc import Iterable
import jsondb
from concurrent.futures import ThreadPoolExecutor

CACHE_DB = jsondb.db.Database('cache_db.json')

def is_type(obj, target_obj):
    if type(target_obj).__name__ == 'str': return type(obj).__name__ == target_obj
    if type(target_obj).__name__ == 'list': return type(obj).__name__ in target_obj
    return False

def handle_division(numerator, denominator, default=0):
    if is_type(numerator, ['int', 'float']) and is_type(denominator, ['int', 'float']):
        return numerator / denominator if denominator != 0 else default
    else:
        return default

def cache_db(key, value=None):
    try:
        return (CACHE_DB.data(key=key) if value is None else CACHE_DB.data(key=key, value=value))
    except:
        return False

def multithread_pool(funcs, max_threads=5):
    executor = ThreadPoolExecutor(max_workers=max_threads)
    processed_args = []
    for func, args in funcs.items():
        arg = [] if args is None or args[0] is None else args[0]
        kwarg = {} if args is None or len(args) == 1 or args[1] is None else args[1]
        processed_args.append(tuple([func, arg, kwarg]))

    threads = [executor.submit(func, *func_args, **func_kwargs)
               for func, func_args, func_kwargs in processed_args]
    return [thread.result() for thread in threads]

def none_safe(object, default=None):
    return object if object is not None else default

def iter_safe(object, default=[]):
    return object if object is not None and isinstance(object, Iterable) else default

def empty_safe(object, default=None):
    return default if object is None or (isinstance(object, Iterable) and not any(object)) else object
