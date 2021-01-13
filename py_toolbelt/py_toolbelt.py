import list_toolbelt as ltb
from forbiddenfruit import curse
list_toolbelt_map = {
    'unique': ltb.list_unique, 'to_tuple': ltb.list_to_tuple, 'to_dict': ltb.list_to_dict,
    'to_set': ltb.list_to_set, 'to_tuple': ltb.list_to_tuple, 'to_dict': ltb.list_to_dict,
    'add': ltb.list_add, 'subtract': ltb.list_subtract, 'multiply': ltb.list_multiply,
    'divide': ltb.list_divide, 'remove_index': ltb.remove_index, 'remove_values': ltb.remove_values,
    'filter': ltb.filter, 'transform': ltb.transform, 'count_all': ltb.count_all,
    'window_enumerate': ltb.window_enumerate, 'compact': ltb.compact, 'intersection': ltb.intersection
}
def patch():
    for function_name, function in list_toolbelt_map.items():
        curse(list, function_name, function)
