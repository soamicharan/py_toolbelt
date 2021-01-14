import py_toolbelt.list_toolbelt as ltb
import py_toolbelt.dict_toolbelt as dtb
import py_toolbelt.other_toolbelt as otb
from forbiddenfruit import curse, reverse
list_toolbelt_map = {
    'unique': ltb.unique, 'to_tuple': ltb.to_tuple, 'to_dict': ltb.to_dict,
    'to_set': ltb.to_set, 'remove_index': ltb.remove_index, 'remove_values': ltb.remove_values,
    'filter': ltb.filter, 'transform': ltb.transform, 'count_all': ltb.count_all,
    'window_enumerate': ltb.window_enumerate, 'compact': ltb.compact,
    'intersection': ltb.intersection, 'flatten': ltb.flat_list, 'get_index': ltb.get_index,
    'execute': ltb.execute
}

dict_toolbelt_map = {
    'transform': dtb.transform, 'keys_list': dtb.keys_list, 'values_list': dtb.values_list,
    'filter': dtb.filter, 'remove': dtb.remove, 'reverse': dtb.reverse, 'deep_merge': dtb.deep_merge
}
def activate():
    for function_name, function in list_toolbelt_map.items():
        curse(list, function_name, function)

    for function_name, function in dict_toolbelt_map.items():
        curse(dict, function_name, function)

    curse(set, 'to_list', otb.set_to_list)
    curse(tuple, 'to_list', otb.tuple_to_list)

    for data_type in [set, list, str, dict, tuple, int, float, type(None)]:
        curse(data_type, 'is_none', otb.is_none)
        curse(data_type, 'is_not_none', otb.is_not_none)

def deactivate():
    for function_name in list_toolbelt_map.keys():
        reverse(list, function_name)

    for function_name in dict_toolbelt_map.keys():
        reverse(dict, function_name)

    reverse(set, 'to_list')
    reverse(tuple, 'to_list')

    for data_type in [set, list, str, dict, tuple, int, float, type(None)]:
        reverse(data_type, 'is_none')
        reverse(data_type, 'is_not_none')
