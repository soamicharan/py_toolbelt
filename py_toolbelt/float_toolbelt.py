import math
def is_positive(self, **kwargs):
    return (kwargs.get('on_true', True) if self > 0 else kwargs.get('on_false', False))

def is_negetive(self, **kwargs):
    return (kwargs.get('on_true', True) if self < 0 else kwargs.get('on_false', False))

def is_zero(self, **kwargs):
    return (kwargs.get('on_true', True) if self == 0 else kwargs.get('on_false', False))

def safe_divide(self, denominator, default=math.nan):
    return (default if denominator == 0 else self / denominator)
