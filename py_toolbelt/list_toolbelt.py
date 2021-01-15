import operator, collections, inspect

def __is_type(obj, target_obj):
    if target_obj == 'iterable': return type(obj).__name__ in ['list', 'set', 'tuple', 'dict']
    if type(target_obj).__name__ == 'str': return type(obj).__name__ == target_obj
    if type(target_obj).__name__ == 'list': return type(obj).__name__ in target_obj
    return False

def __apply_function(function, parameter):
    if function.__dict__.get('__args_length__', 1) == 1:
        return function(parameter)
    else:
        return function(*parameter)

def __get_args(function):
    if function is not None:
        function.__dict__['__args_length__'] = len(inspect.getargspec(function).args)

def __evaluate_condition(condition, element, inverse=False):
    if condition is None: return not inverse
    return inverse ^ __apply_function(condition, element)

def __apply_condition_cast(self, **kwargs):
    __get_args(kwargs.get('condition'))
    if kwargs.get('condition') or not kwargs.get('cast'):
        return [kwargs.get('cast')(element) if kwargs.get('cast') else element \
                for element in self \
                if __evaluate_condition(kwargs.get('condition'), element, kwargs.get('inverse', False))]
    else:
        return self



def unique(self):
    return [*{*self}]

def to_set(self):
    return {*self}

def to_tuple(self):
    return (*self, )

def to_dict(self, key_function, value_function):
    __get_args(key_function)
    __get_args(value_function)
    return {__apply_function(key_function, element): __apply_function(value_function, element) for element in self}

def remove_index(self, index=[], **kwargs):
    if index == [] and not kwargs.get('condition'):
        return self
    elif isinstance(index, int):
        index = [index]

    conditional_index = __apply_condition_cast(
        [*range(len(self))], condition=kwargs.get('condition')
    ) if kwargs.get('condition') else []
    return __apply_condition_cast(
        [element for index_value, element in enumerate(self) \
         if index_value not in index + conditional_index],
        cast=kwargs.get('cast')
    )

def remove_values(self, values=[], **kwargs):
    if values == [] and not kwargs.get('condition'):
        return self
    elif values == [] and kwargs.get('condition'):
        return __apply_condition_cast(self, inverse=True, **kwargs)

    return __apply_condition_cast(
        [element for element in self if element not in values], inverse=True, **kwargs
    )

def filter(self, condition, **kwargs):
    return __apply_condition_cast(self, condition=condition, cast=kwargs.get('cast'))

def compact(self):
    compact_condition = lambda element: element is not None or (__is_type(element, 'iterable') and any(element))
    return __apply_condition_cast(self, condition=compact_condition)

def transform(self, element_function):
    return [__apply_function(element_function, element) for element in self]

def count_all(self):
    return {**collections.Counter(self)}

def intersection(self, target_object):
    return [*({*self}.intersection({*target_object}))]

def flatten(self):
    flatten_list = []
    for element in self:
        if isinstance(element, list):
            flatten_list.extend(flatten(element))
        elif isinstance(element, tuple) or isinstance(element, set):
            flatten_list.extend(flatten([*element]))
        else:
            flatten_list.append(element)

    return flatten_list

def get_index(self, index, default_value=None):
    try:
        return self[index]
    except IndexError:
        return default_value

def execute(self, execute_function):
    __get_args(execute_function)
    for element in self:
        __apply_function(execute_function, element)

    return self
