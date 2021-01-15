import operator, inspect

def __apply_function(function, parameter):
    if function.__dict__.get('__args_length__', 1) == 1:
        return function(parameter)
    else:
        return function(*parameter)

def __get_args(function):
    if function is not None:
        function.__dict__['__args_length__'] = len(inspect.getargspec(function).args)

def __evaluate_condition(condition, element, inverse=False):
    if not condition: return not inverse
    return inverse ^ condition(*element)

def __apply_condition(self, **kwargs):
    if kwargs.get('condition'):
        return {key: value for key, value in self.items() \
                if __evaluate_condition(
                    kwargs.get('condition'), (key, value), kwargs.get('inverse', False)
                )}
    return self


def transform(self, key_function=None, value_function=None):
    key_function = key_function if key_function is not None else lambda element: element
    value_function = value_function if value_function is not None else lambda element: element
    __get_args(key_function)
    __get_args(value_function)
    return {__apply_function(key_function, key): __apply_function(value_function, value) \
            for key, value in self.items()}

def keys_list(self):
    return [*self]

def values_list(self):
    return [*self.values()]

def filter(self, condition):
    return __apply_condition(self, condition=condition)

def remove(self, key_function=None, value_function=None, operator='and'):
    operator = operator.and_ if operator == 'and' else operator.or_
    key_function = key_function if key_function is not None else lambda element: True
    value_function = value_function if value_function is not None else lambda element: True
    __get_args(key_function)
    __get_args(value_function)
    return {key: value for key, value in self \
            if operator(__apply_function(key_function, key), __apply_function(value_function, value))}

def reverse(self, keep_duplicate=False):
    if not keep_duplicate:
        return {value: key for key, value in self.items()}
    else:
        reverse_dict, duplicate_value = {}, []
        for key, value in self.items():
            if value in reverse_dict:
                if value in duplicate_value:
                    reverse_dict[value].append(key)
                else:
                    reverse_dict[value] = [reverse_dict[value], key]
                    duplicate_value.append(value)
            else:
                reverse_dict[value] = key

        return reverse_dict

def deep_merge(self, target_dict, max_depth=None, depth=1):
    merged_dict = self.copy()
    for key, value in target_dict.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], dict) and isinstance(value, dict):
                if max_depth is not None and max_depth == depth:
                    merged_dict[key] = [merged_dict[key], value]
                else:
                    merged_dict[key] = deep_merge(merged_dict[key], value, max_depth, depth + 1)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value

    return merged_dict

def execute(self, execute_function):
    for key, value in self.items():
        execute_function(key, value)

    return self
