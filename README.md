# Py ToolBelt
This module contains basic functions for built-in datatypes for execute trivial tasks.
This functions are available as built-in datatype methods.

## Installation
Install package using pip -> `pip install py-toolbelt`

## Usage
Import the module and activate toolbelt
`
import py_toolbelt
py_toolbelt.activate()
`
After activation, custom functions are available as built-in methods.
For example -
Before activation, in python console, create a list variable `list_object = [1, 2, 3]` and type `list_object.` and press tab to get prompt of available methods, you see -
```python
>>> list_object.
l.append(   l.clear(    l.copy(     l.count(    l.extend(   l.index(    l.insert(   l.pop(      l.remove(   l.reverse(  l.sort(
```

After activation -
```python
>>> list_object.
l.append(         l.count(          l.filter(         l.insert(         l.pop(            l.reverse(        l.to_tuple(
l.clear(          l.count_all(      l.flat_list(      l.intersection(   l.remove(         l.sort(           l.transform(
l.compact(        l.execute(        l.get_index(      l.is_none(        l.remove_index(   l.to_dict(        l.unique(
l.copy(           l.extend(         l.index(          l.is_not_none(    l.remove_values(  l.to_set(
```

To deactivate the toolbelt
`
py_toolbelt.deactivate()
`

## Available Functions
### List
#### unique()
Eliminate duplicate elements from list.<br>
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
```python
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.unique())
[1, 2, 3]
```

### to_set()
Convert list to set.<br>
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
```python
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.to_set())
{1, 2, 3}
```

### to_tuple()
Convert list to tuple.<br>
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
```python
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.to_tuple())
(1, 2, 3, 3, 2)
```

### to_dict(`key_function`=None, `value_function`=None)
Convert list to dict with with keys using `key_function` and values using `value_function`.
**Argument**
* __key_function__- `function`, any number of argument are accepted. (_required_)
* __value_function__ - `function`, any number of arguments are accepted. (_required_)

**Example**
```python
>>> list_obj = [1, 2, 3, 4]
>>> list_obj.to_dict(key_function=lambda x: x, value_function=lambda y: y * 2)
{1: 1, 2: 4, 3: 6, 4: 8}
```

### remove_index(`index`=[], `**kwargs`)
Remove indexes from list based on given index values in `index` argument and given `condition` keyword argument.
_**note - ** `condition` is applicable on indexes, not on the elements of list_
**Arguments**
* __index__ - `list` / `int`, if single `int` is given then remove that index, if `list` is given then remove indexes given in list. (_optional_, _default: `[]`_)

**Keyword arguments**
* __condition__ - `function`, if condition function satisfy for index number then it will be removed.
* __cast__ - `data_type`, cast the elements of list.

**Example**
```python
>>> list_obj = ['hello', 'this', 'is', 'a', 'list']
>>> list_obj.remove_index(1)
['hello', 'is', 'a', 'list']

>>> list_obj.remove_index([0, 1, 2])
['a', 'list']

>>> list_obj.remove_index(condition=lambda x: x % 2 == 0) # even indexes will be removed
['is', 'list']

>>> list_obj = [1, 2, 3, 4]
>>> list_obj.remove_index([1, 2], condition=lambda x: x % 2 == 0, cast=str)
['4']
```

### remove_values(`values`=[], `**kwargs`)
Remove elements from list based on given values in `index` argument and given `condition` keyword argument.

**Arguments**
* __values__ - `list` / any data type, if any other data type is given (except list) then it exclude all occurences, if `list` is given then exclude elements if it exist in given list. (_optional_, _default: `[]`_)

**Keyword arguments**
* __condition__ - `function`, if condition function satisfy for list element then it will be removed.
* __cast__ - `data_type`, cast the elements of list.

**Example**
```python
>>> list_obj = ['hello', 'this', 'is', 'a', 'list']
>>> list_obj.remove_values('this')
['hello', 'is', 'a', 'list']

>>> list_obj.remove_values(['hello', 'this', 'is'])
['a', 'list']

>>> list_obj.remove_values(condition=lambda x: x == 'hello')
['this', 'is', 'a', 'list']

>>> list_obj = [1, 2, 3, 4]
>>> list_obj.remove_values([1, 2], condition=lambda x: x % 2 == 0, cast=str)
['4']
```

### filter(`condition`, `**kwargs`)
Filter list with given `condition` function.
It is equivalent to - `[element for element in list_object if condition(element)]`
**Arguments**
* __condition__ - `function`, if condition function not satisfy for list element then it will be excluded. (_required_)

**Keyword arguments**
* __cast__ - `data_type`, cast the elements of list.

**Example**
```python
>>> list_obj = [1, 2, 3, 4, 5, 6]
>>> list_obj.filter(lambda x: x > 3)
[4, 5, 6]

>>> list_obj.filter(lambda x: x <= 3, cast=float)
[1.0. 2.0. 3.0]
```

### compact()
Exclude `None` or empty `list` / `dict` / `set` / `tuple` from list.

**Example**
```python
>>> list_obj = [1, 2, 3, None, [], {}]
>>> list_obj.compact()
[1, 2, 3]
```

### transform(`element_function`)
Transform the elements of list.

**Arguments**
* __element_function__ - `function`, list elements are passed to given function. (_required_)

**Example**
```python
>>> list_obj = [1, 2, 3, 4]
>>> list_obj.transform(lambda x: x ** 2)
[1, 4, 9, 16]

>>> list_obj = [*enumerate(list_object)]
>>> list_obj.transform(lambda x, y: x + y)
[1, 3, 5, 7]
```

### count_all()
Count occurences of elements in list.<br>
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
```python
>>> list_obj = [1, 2, 2, 3, 3, 4]
>>> list_obj.count_all()
{1: 1, 2: 2, 3: 2, 4: 1}
```

### intersection(`target_list`)
Give list of common elements.<br>
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
```python
>>> list_obj = [1, 2, 2, 3, 3, 4]
>>> list_obj.intersection([2, 4, 5, 6, 7])
[2, 4]
```

### flatten()
Convert N-Dimention list into single flat 1-D list.

**Example**
```python
>>> list_obj = [1, [2, 2], 3, [[[3]]], 4]
>>> list_obj.flatten()
[1, 2, 2, 3, 3, 4]
```

### get_index(`index`, `default_value=None`)
Fetch given index from list, if given index is out of range then return `default_value`.

**Arguments**
* __index__ - `int`, (_required_)
* __default_value__ - any data type, (_optional_, _default: None_)

**Example**
```python
>>> list_obj = [1, 2, 3, 4, 5]
>>> list_obj.get_index(2)
3

>>> list_obj.get_index(10, 'N/A')
N/A
```

### execute(`execute_function`)
Execute function using elements of list.

**Arguments**
* __execute_function__ - `function`, it can accept any number of arguments (_required_)

**Example**
```python
>>> list_obj = [1, 2, 3, 4, 5]
>>> new_list = []
>>> list_obj.execute(lambda x: new_list.append(x * 3))
>>> new_list
[3, 6, 9, 12, 15]

>>> list_obj.execute(lambda x: print(x))
1
2
3
4
5
```

## Dict
### filter(`condition`, `**kwargs`)
Filter dict based on keys and values.
**Arguments**
* __condition__ - `function`, `function` must accept 2 parameters, 1st parameter for key and 2nd parameter for value. (_required_)

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3}
>>> dict_obj.filter(lambda key, value: value > 1)
{'b': 2, 'c': 3}
```

### transform(`key_function=None`, `value_function=None`)
Transform dict keys and values according to given functions.
**Arguments**
* __key_function__ - `function`, `function` can accept any number of arguments. (_optional_, _default: `None`_)
* __value_function__ - `function`, `function` can accept any number of arguments. (_optional_, _default: `None`_)

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3}
>>> dict_obj.transform(key_function=lambda x: 'a' + x)
{'aa': 1, 'ab': 2, 'ac': 3}

>>> dict_obj.transform(value_function=lambda x: x ** 2)
{'a': 1, 'b': 4, 'c': 9}

>>> dict_obj = {'a': (1, 2), 'b': (3, 4), 'c': (5, 6)}
>>> dict_obj.transform(key_function=lambda key: key + '_sum', value_function=lambda x, y: x + y)
{'a_sum': 3, 'b_sum': 7, 'c_sum': 11}
```

### keys_list()
Return keys of dict as list.

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3}
>>> dict_obj.keys_list()
['a', 'b', 'c']
```

### values_list()
Return values of dict as list.

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3}
>>> dict_obj.values_list()
[1, 2, 3]
```

### remove(`key_function=None`, `value_function=None`, `operator='and'`)
Remove dict keys based on given `key_function` and `value_fucntion` and operation between `key_funciton` and `value_function` which is by default `and` operation.
**Arguments**
* __key_function__ - `function`, `function` can accept any number of arguments. (_optional_, _default: `None`_)
* __value_function__ - `function`, `function` can accept any number of arguments. (_optional_, _default: `None`_)
* __operator__ - `str`, accepted string - ['and', 'or'], (_optional_, _default='and'_)

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3}
>>> dict_obj.remove(key_function=lambda x: x == 'b')
{'a': 1, 'c': 3}

>>> dict_object.remove(key_function=lambda key: key in ['b', 'c'], value_fucntion=lambda value: value % 2 == 1)
{'a': 1, 'b': 2}

>>> dict_object.remove(key_function=lambda key: key in ['b', 'c'], value_fucntion=lambda value: value % 2 == 1, operator='or')
{'a': 1}
```

### reverse(`keep_duplicate=False`)
Reverse the dict, set values as keys and keys as values. If `keep_duplicate` is set true then it will merge duplicate value as list.<br>
_**note -** dict values should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Arguments**
* __keep_duplicate__ - `bool`, (_optional_, _default: `False`_)

**Example**
```python
>>> dict_obj = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
>>> dict_obj.reverse()
{1: 'a', 2: 'b', 3: 'd'}

>>> dict_obj.reverse(keep_duplicate=True)
{1: 'a', 2: 'b', 3: ['c', 'd']}
```

### deep_merge(`target_dict`, `max_depth=None`)
It will merge given `target_dict` with given `max_depth`. If `max_depth` is `None` then it go down to maximum depth for merging.
**Arguments**
* __target_dict__ - `dict`, (_required_)
* __max_depth__ - `int`, `int` greater than 0, (_optional_, _default: `None`_)

**Example**
```python
>>> dict_obj = {'a': 1, 'b': {'c': {'d': 3}, 'e': 2}}
>>> dict_obj.deep_merge({'g': 4, 'b': {'c': {'d': 5}}})
{'a': 1, 'b': {'c': {'d': [3, 5]}, 'e': 2}, 'g': 4}

>>> dict_obj.deep_merge({'g': 4, 'b': {'c': {'d': 5}}}, max_depth=1)
{'a': 1, 'b': [{'c': {'d': 3}, 'e': 2}, {'c': {'d': 5}}], 'g': 4}
```

## Set
### to_list()
Convert set to list.

## Tuple
### to_list()
Convert tuple to list.

## Int & Float
### is_positive(`**kwargs`)
Return `True` if number is positive else return `False`. If `on_true` or `on_false` keyword arguments are present then it will return keyword argument value respectively.

**Keyword arguments**
* __on_true__ - any data type, (_optional_, _default: `True`_)
* __on_false__ - any data type, (_optional_, _default: `False`_)

**Example**
```python
>>> num = 1
>>> num.is_positive()
True
>>> num.is_positive(on_true='Yes')
Yes
>>> num = -9
>>> num.is_positive(on_false='No')
No
>>> num.is_positive(on_true='Yes')
False
```

### is_negetive(`**kwargs`)
Return `True` if number is negetive else return `False`. If `on_true` or `on_false` keyword arguments are present then it will return keyword argument value respectively.

**Keyword arguments**
* __on_true__ - any data type, (_optional_, _default: `True`_)
* __on_false__ - any data type, (_optional_, _default: `False`_)

**Example**
```python
>>> num = 1
>>> num.is_negetive()
False
>>> num.is_negetive(on_true='Yes')
False
>>> num = -9
>>> num.is_negetive(on_false='No')
True
>>> num.is_negetive(on_true='Yes', on_false='No')
Yes
```

### is_zero(`**kwargs`)
Return `True` if number is equal to zero else return `False`. If `on_true` or `on_false` keyword arguments are present then it will return keyword argument value respectively.

**Keyword arguments**
* __on_true__ - any data type, (_optional_, _default: `True`_)
* __on_false__ - any data type, (_optional_, _default: `False`_)

**Example**
```python
>>> num = 1
>>> num.is_zero()
False
>>> num.is_zero(on_true='Yes')
False
>>> num = 0
>>> num.is_zero(on_false='No')
True
>>> num.is_zero(on_true='Yes', on_false='No')
Yes
```

### safe_divide(`denominator`, `default=math.nan`)
It ensure if `denominator` is zero then return `default` value otherwise return divided value.
**Arguments**
* __denominator__ - `int` / `float`, (_required_)
* __default__ - any data type, (_optional_, _default: `math.nan`_)

**Example**
```python
>>> a = 4
>>> a.safe_divide(2)
2.0
>>> a.safe_divide(0)
nan
>>> a.safe_divide(0, 0)
0
>>> a.safe_divde(0, 'N/A')
N/A
```

## Others
This is common to all data types -
### is_none()
Return `True` if object is `None` else return `False`. If `on_true` or `on_false` keyword arguments are present then it will return keyword argument value respectively.

**Keyword arguments**
* __on_true__ - any data type, (_optional_, _default: `True`_)
* __on_false__ - any data type, (_optional_, _default: `False`_)

**Example**
```python
>>> a, b, c, d = 2, 'hello', [], None
>>> a.is_none()
False
>>> a.is_none(on_false=a + 1)
3
>>> b.is_none(on_true="Yes")
False
>>> d.is_none()
True
```

### is_not_none()
Return `True` if object is not `None` else return `False`. If `on_true` or `on_false` keyword arguments are present then it will return keyword argument value respectively.

**Keyword arguments**
* __on_true__ - any data type, (_optional_, _default: `True`_)
* __on_false__ - any data type, (_optional_, _default: `False`_)

**Example**
```python
>>> a, b, c, d = 2, 'hello', [], None
>>> a.is_not_none()
True
>>> a.is_not_none(on_false=a + 1)
True
>>> b.is_not_none(on_true="Yes")
Yes
>>> d.is_not_none()
False
```

# MIT License

Copyright (c) 2021 Soami Charan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
