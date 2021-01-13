import numpy as np
import operator, collections

def is_type(obj, target_obj):
    if type(target_obj).__name__ == 'str': return type(obj).__name__ == target_obj
    if type(target_obj).__name__ == 'list': return type(obj).__name__ in target_obj
    return False

def evaluate_condition(condition, element, negetive=False):
    return (not condition(element) if negetive else condition(element))

def condition_cast(list_object, negetive=False, **kwargs):
    if kwargs.get('condition') and not kwargs.get('cast'):
        return [element for element in list_object if evaluate_condition(kwargs.get('condition'), element, negetive)]
    elif kwargs.get('cast') and not kwargs.get('condition'):
        return [kwargs.get('cast')(element) for element in list_object]
    elif kwargs.get('cast') and kwargs.get('condition'):
        return [kwargs.get('cast')(element) for element in list_object if evaluate_condition(kwargs.get('condition'), element, negetive)]
    else:
        return list_object

def list_unique(list_object, **kwargs):
    return [*{*condition_cast(list_object, **kwargs)}]

def list_to_set(list_object, **kwargs):
    return {*condition_cast(list_object, **kwargs)}

def list_to_tuple(list_object, **kwargs):
    return (*condition_cast(list_object, **kwargs), )

def list_to_dict(list_object, key, value, **kwargs):
    return {key(element): value(element) for element in condition_cast(list_object, **kwargs)}

def list_operation(list_object, operation, target_list=None, **kwargs):
    operator_const = lambda value_tuple: operation(operation(*value_tuple), kwargs.get('const')) if 'const' in kwargs else operation(*value_tuple)
    if target_list is None and 'const' not in kwargs:
        return list_object
    elif target_list is None and 'const' in kwargs:
        return [operation(element, kwargs.get('const')) for element in list_object]

    if len(list_object) == len(target_list):
        return [operator_const(value_tuple) for value_tuple in zip(short_list, long_list)]

    short_list = list_object if len(list_object) < len(target_list) else target_list
    long_list = list_object if len(list_object) >= len(target_list) else target_list
    if 'pad' in kwargs:
        short_list += [kwargs.get('pad') for _ in range(abs(len(list_object) - len(target_list)))]
        return [operator_const(value_tuple) for value_tuple in zip(short_list, long_list)]

    residue_long_list = [operation(element, kwargs.get('const')) if 'const' in kwargs else element for element in long_list[len(short_list):]]
    return condition_cast([operator_const(value_tuple) for value_tuple in zip(short_list, long_list)] + residue_long_list, **kwargs)

def list_add(list_object, target_list=None, **kwargs):
    return list_operation(list_object, operator.add, target_list, **kwargs)

def list_multiply(list_object, target_list=None, **kwargs):
    return list_operation(list_object, operator.mul, target_list, **kwargs)

def list_subtract(list_object, target_list=None, **kwargs):
    return list_operation(list_object, operator.sub, target_list, **kwargs)

def list_divide(list_object, target_list=None, **kwargs):
    return list_operation(list_object, operator.truediv, target_list, **kwargs)

def remove_index(list_object, index=[], **kwargs):
    if index == [] and not kwargs.get('condition'):
        return list_object
    elif isinstance(index, int):
        index = [index]

    conditional_index = condition_cast([*range(len(list_object))], condition=kwargs.get('condition')) if kwargs.get('condition') else []
    return condition_cast([element for index_value, element in enumerate(list_object) if index_value not in index + conditional_index], cast=kwargs.get('cast'))

def remove_values(list_object, values=[], **kwargs):
    if values == [] and not kwargs.get('condition'):
        return list_object
    elif values == [] and kwargs.get('condition'):
        return condition_cast(list_object, negetive=True, **kwargs)

    return condition_cast([element for element in list_object if element not in values], negetive=True, **kwargs)

def filter(list_object, condition, **kwargs):
    return condition_cast(list_object, condition=condition, cast=kwargs.get('cast'))

def compact(list_object):
    return condition_cast(list_object, condition=lambda element: element is not None or (is_type(element, ['list', 'set', 'tuple', 'dict']) and any(element)))

def transform(list_object, value, **kwargs):
    return condition_cast([value(element) for element in list_object], **kwargs)

def count_all(list_object, **kwargs):
    return {**collections.Counter(condition_cast(list_object, **kwargs))}

def window_enumerate(list_object, length, increment=1, pad=None, **kwargs):
    window_list = []
    start, end = 0, length
    list_length = len(list_object)
    for index in range(0, list_length, increment):
        if (index + length) > list_length:
            break
        window_list.append(list_object[index:index + length])

    if (index + 1) < list_length:
        window_list.append(list_object[index:] + [pad for _ in range(length - (list_length - index))])

    return window_list

def intersection(list_object, target_object):
    return [*({*list_object}.intersection({*target_object}))]
