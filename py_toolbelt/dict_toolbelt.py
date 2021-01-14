import operator

def __evaluate_condition(condition, element, negetive=False):
    return (not condition(*element) if negetive else condition(*element))

def __apply_condition(dict_object, negetive=False, **kwargs):
    if kwargs.get('condition'):
        return {key: value for key, value in dict_object.items() if __evaluate_condition(kwargs.get('condition'), (key, value), negetive)}
    return dict_object

def transform(dict_object, key_function=None, value_function=None, **kwargs):
    key_function = key_function if key_function is not None else lambda element: element
    value_function = value_function if value_function is not None else lambda element: element
    return __apply_condition({key_function(key): value_function(value) for key, value in dict_object.items()}, **kwargs)

def keys_list(dict_object, **kwargs):
    return [*__apply_condition(dict_object, **kwargs)]

def values_list(dict_object, **kwargs):
    return [*__apply_condition(dict_object, **kwargs).values()]

def filter(dict_object, **kwargs):
    return __apply_condition(dict_object, **kwargs)

def remove(dict_object, key_function=None, value_function=None, operator='and', **kwargs):
    operator = operator.and_ if operator == 'and' else operator.or_
    key_function = key_function if key_function is not None else lambda element: True
    value_function = value_function if value_function is not None else lambda element: True
    return __apply_condition({key: value for key, value in dict_object if operator(key_function(key), value_function(value))}, **kwargs)

def reverse(dict_object, keep_duplicate=False, **kwargs):
    if not keep_duplicate:
        return __apply_condition({value: key for key, value in dict_object.items()}, **kwargs)
    else:
        reverse_dict, duplicate_value = {}, []
        for key, value in dict_object.items():
            if value in reverse_dict:
                if value in duplicate_value:
                    reverse_dict[value].append(key)
                else:
                    reverse_dict[value] = [reverse_dict[value], key]
            else:
                reverse_dict[value] = key

        return __apply_condition(reverse_dict, **kwargs)

def deep_merge(dict_object, target_dict, max_depth=None, **kwargs):
    depth = kwargs.get('depth', 1)
    merged_dict = dict_object.copy()
    for key, value in target_dict.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], dict) and isinstance(value, dict):
                if max_depth is not None and max_depth == depth:
                    merged_dict[key] = [merged_dict[key], value]
                else:
                    merged_dict[key] = deep_merge(merged_dict[key], value, max_depth=max_depth, depth=depth+1)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    if kwargs.get('condition'):
        return __apply_condition(merged_dict, **kwargs)
    else:
        return merged_dict
