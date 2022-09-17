def is_not_none(object=None, **kwargs):
    return (kwargs.get('on_true', True) if object is not None else kwargs.get('on_false', False))

def is_none(object=None, **kwargs):
    return (kwargs.get('on_true', True) if object is None else kwargs.get('on_false', False))

@property
def safe_access(self):
    class wrapper:
        def __init__(inner_self, obj):
            inner_self.__obj = obj
        
        def __getattr__(inner_self, name):
            try:
                return getattr(inner_self.__obj, name)
            except AttributeError:
                return None
        
        def __call__(inner_self, *args, **kwds):
            return inner_self.__obj(*args, **kwds)

    return wrapper(self)

def safe_none_accessor():
    class wrapper:
        def __getattr__(self, name):
            return None
        
        def __call__(self, *args, **kwargs):
            return None
    
    return wrapper()