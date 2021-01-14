import operator, collections, inspect

def __is_type(obj, target_obj):
    if target_obj == 'iterable': return type(obj).__name__ in ['list', 'set', 'tuple', 'dict']
    if type(target_obj).__name__ == 'str': return type(obj).__name__ == target_obj
    if type(target_obj).__name__ == 'list': return type(obj).__name__ in target_obj
    return False

def __apply_function(function, parameter):
    if function.__dict__.get('args_length', 1) == 1:
        return function(parameter)
    else:
        return function(*parameter)

def __get_args(function):
    if function is not None:
        function.__dict__['args_length'] = len(inspect.getargspec(function).args)

def __evaluate_condition(condition, element, negetive=False):
    if condition is None: return not negetive
    return negetive ^ __apply_function(condition, element)

def __apply_condition_cast(list_object, negetive=False, **kwargs):
    __get_args(kwargs.get('condition'))
    if kwargs.get('condition') or not kwargs.get('cast'):
        return [kwargs.get('cast')(element) if kwargs.get('cast') else element \
                for element in list_object \
                if __evaluate_condition(kwargs.get('condition'), element, negetive)]
    else:
        return list_object



def unique(list_object, **kwargs):
    return [*{*__apply_condition_cast(list_object, **kwargs)}]

def to_set(list_object, **kwargs):
    return {*__apply_condition_cast(list_object, **kwargs)}

def to_tuple(list_object, **kwargs):
    return (*__apply_condition_cast(list_object, **kwargs), )

def to_dict(list_object, key_function, value_function, **kwargs):
    __get_args(key_function)
    __get_args(value_function)
    return {__apply_function(key_function, element): __apply_function(value_function, element) \
            for element in __apply_condition_cast(list_object, **kwargs)}

def remove_index(list_object, index=[], **kwargs):
    if index == [] and not kwargs.get('condition'):
        return list_object
    elif isinstance(index, int):
        index = [index]

    conditional_index = __apply_condition_cast(
        [*range(len(list_object))], condition=kwargs.get('condition')
    ) if kwargs.get('condition') else []
    return __apply_condition_cast(
        [element for index_value, element in enumerate(list_object) \
         if index_value not in index + conditional_index],
        cast=kwargs.get('cast')
    )

def remove_values(list_object, values=[], **kwargs):
    if values == [] and not kwargs.get('condition'):
        return list_object
    elif values == [] and kwargs.get('condition'):
        return __apply_condition_cast(list_object, negetive=True, **kwargs)

    return __apply_condition_cast(
        [element for element in list_object if element not in values], negetive=True, **kwargs
    )

def filter(list_object, condition, **kwargs):
    return __apply_condition_cast(list_object, condition=condition, cast=kwargs.get('cast'))

def compact(list_object):
    compact_condition = lambda element: element is not None or (__is_type(element, 'iterable') and any(element))
    return __apply_condition_cast(list_object, condition=compact_condition)

def transform(list_object, value, **kwargs):
    return __apply_condition_cast(
        [__apply_function(value, element) for element in list_object], **kwargs
    )

def count_all(list_object, **kwargs):
    return {**collections.Counter(__apply_condition_cast(list_object, **kwargs))}

def window_enumerate(list_object, length, increment=1, pad=None):
    window_list, list_length = [], len(list_object)
    for index in range(0, list_length, increment):
        if (index + length) > list_length:
            break
        window_list.append(list_object[index:index + length])

    if (index + 1) < list_length:
        window_list.append(list_object[index:] + [pad for _ in range(length - (list_length - index))])

    return window_list

def intersection(list_object, target_object):
    return [*({*list_object}.intersection({*target_object}))]

def flat_list(list_object):
    flatten_list = []
    for element in list_object:
        if isinstance(element, list):
            flatten_list.extend(flat_list(element))
        else:
            flatten_list.append(element)

    return flatten_list

def get_index(list_object, index, default_value=None):
    try:
        return list_object[index]
    except IndexError:
        return default_value

def execute(list_object, execute_function, **kwargs):
    __get_args(execute_function)
    for element in __apply_condition_cast(list_object, condition=kwargs.get('condition')):
        __apply_function(execute_function, element)

    return list_object
