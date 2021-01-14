def set_to_list(set_object):
    return [*set_object]

def tuple_to_list(tuple_object):
    return [*tuple_object]

def is_not_none(object=None, **kwargs):
    if object is not None:
        return (True if 'on_true' not in kwargs else kwargs.get('on_true'))
    else:
        return (False if 'on_false' not in kwargs else kwargs.get('on_false'))

def is_none(object=None, **kwargs):
    if object is None:
        return (True if 'on_true' not in kwargs else kwargs.get('on_true'))
    else:
        return (False if 'on_false' not in kwargs else kwargs.get('on_false'))
