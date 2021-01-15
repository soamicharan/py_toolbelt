def is_not_none(object=None, **kwargs):
    return (kwargs.get('on_true', True) if object is not None else kwargs.get('on_false', False))

def is_none(object=None, **kwargs):
    return (kwargs.get('on_true', True) if object is None else kwargs.get('on_false', False))
