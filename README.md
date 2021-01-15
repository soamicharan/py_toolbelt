#Py ToolBelt
This module contains basic functions for built-in datatypes for execute trivial tasks.
This functions are available as built-in datatype methods.

##Installation
Install package using pip -> `pip install py-toolbelt`

##Usage
Import the module and activate toolbelt
`
import py_toolbelt
py_toolbelt.activate()
`
After activation, custom functions are available as built-in methods.
For example -
Before activation, in python console, create a list variable `list_object = [1, 2, 3]` and type `list_object.` and press tab to get prompt of available methods, you see -
`
>>> list_object.
l.append(   l.clear(    l.copy(     l.count(    l.extend(   l.index(    l.insert(   l.pop(      l.remove(   l.reverse(  l.sort(
`

After activation -
`
>>> list_object.
l.append(         l.count(          l.filter(         l.insert(         l.pop(            l.reverse(        l.to_tuple(
l.clear(          l.count_all(      l.flat_list(      l.intersection(   l.remove(         l.sort(           l.transform(
l.compact(        l.execute(        l.get_index(      l.is_none(        l.remove_index(   l.to_dict(        l.unique(
l.copy(           l.extend(         l.index(          l.is_not_none(    l.remove_values(  l.to_set(
`

To deactivate the toolbelt
`
py_toolbelt.deactivate()
`

##Available Functions
###List
####unique()
Eliminate duplicate elements from list.
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
`
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.unique())
[1, 2, 3]
`

###to_set()
Convert list to set.
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
`
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.to_set())
{1, 2, 3}
`

###to_tuple()
Convert list to tuple.
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
`
>>> list_obj = [1, 2, 3, 3, 2]
>>> print(list_obj.to_tuple())
(1, 2, 3, 3, 2)
`

###to_dict(key_function=None, value_function=None)
Convert list to dict with with keys using `key_function` and values using `value_function`.
**Argument**
* __key_function__- `function`, any number of argument are accepted. (_required_)
* __value_function__ - `function`, any number of arguments are accepted. (_required_)

**Example**
`
>>> list_obj = [1, 2, 3, 4]
>>> list_obj.to_dict(key_function=lambda x: x, value_function=lambda y: y * 2)
{1: 1, 2: 4, 3: 6, 4: 8}
`

###remove_index(index=[], **kwargs)
Remove indexes from list based on given index values in `index` argument and given `condition` keyword argument.
_**note - ** `condition` is applicable on indexes, not on the elements of list_
**Arguments**
* __index__ - `list` / `int`, if single `int` is given then remove that index, if `list` is given then remove indexes given in list. (_optional_, _default: []_)

**Keyword arguments**
* __condition__ - `function`, if condition function satisfy for index number then it will be removed.
* __cast__ - `data_type`, cast the elements of list.

**Example**
`
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
`

###remove_values(values=[], **kwargs)
Remove elements from list based on given values in `index` argument and given `condition` keyword argument.

**Arguments**
* __values__ - `list` / any data type, if any other data type is given (except list) then it exclude all occurences, if `list` is given then exclude elements if it exist in given list. (_optional_, _default: []_)

**Keyword arguments**
* __condition__ - `function`, if condition function satisfy for list element then it will be removed.
* __cast__ - `data_type`, cast the elements of list.

**Example**
`
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
`

###filter(condition, **kwargs)
Filter list with given `condition` function.
It is equivalent to - `[element for element in list_object if condition(element)]`
**Arguments**
* __condition__ - `function`, if condition function not satisfy for list element then it will be excluded. (_required_)

**Keyword arguments**
* __cast__ - `data_type`, cast the elements of list.

**Example**
`
>>> list_obj = [1, 2, 3, 4, 5, 6]
>>> list_obj.filter(lambda x: x > 3)
[4, 5, 6]

>>> list_obj.filter(lambda x: x <= 3, cast=float)
[1.0. 2.0. 3.0]

`
###compact()
Exclude `None` or empty `list` / `dict` / `set` / `tuple` from list.

**Example**
`
>>> list_obj = [1, 2, 3, None, [], {}]
>>> list_obj.compact()
[1, 2, 3]
`

###transform(element_function)
Transform the elements of list.

**Arguments**
* __element_function__ - `function`, list elements are passed to given function. (_required_)

**Example**
`
>>> list_obj = [1, 2, 3, 4]
>>> list_obj.transform(lambda x: x ** 2)
[1, 4, 9, 16]

>>> list_obj = [*enumerate(list_object)]
>>> list_obj.transform(lambda x, y: x + y)
[1, 3, 5, 7]
`

###count_all()
Count occurences of elements in list.
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
`
>>> list_obj = [1, 2, 2, 3, 3, 4]
>>> list_obj.count_all()
{1: 1, 2: 2, 3: 2, 4: 1}

`

###intersection(target_list)
Give list of common elements.
_**note -** elements should be hashable datatype i.e elements must be str, int, float, tuple, bool only._

**Example**
`
>>> list_obj = [1, 2, 2, 3, 3, 4]
>>> list_obj.intersection([2, 4, 5, 6, 7])
[2, 4]

`
###flatten()
Convert `N`-D list into single flat 1-D list.

**Example**
`
>>> list_obj = [1, [2, 2], 3, [[[3]]], 4]
>>> list_obj.flatten()
[1, 2, 2, 3, 3, 4]

`

###get_index(index, default_value=None)
Fetch given index from list, if given index is out of range then return `default_value`.

**Arguments**
* __index__ - `int`, (_required_)
* __default_value__ - any data type, (_optional_, _default: None_)

**Example**
`
>>> list_obj = [1, 2, 3, 4, 5]
>>> list_obj.get_index(2)
3

>>> list_obj.get_index(10, 'N/A')
N/A

`

###execute(execute_function)
Execute function using elements of list.

**Arguments**
* __execute_function__ - `function`, it can accept any number of arguments (_required_)

**Example**
`
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

`
