Go to `py_toolbelt/py_toolbelt` folder
Open a python console there.
For list only -
Create a python list. For example `l = [1, 2, 3, 4]`
Write `l.` then press tab, it will prompt list builtin methods.
now import `import py_toolbelt as ptb`
Call patch function `ptb.patch()`
Now again write `l.` then press tab, this time you see lots of other custom functions as builtin function in prompt list.
For example - convert a list to set -`l.to_set()`, cast elements to str - `l.to_set(cast=str)`
filter anything - `l.filter(lambda x: x < 2)`
I know there are already existing function like `filter()`, `map()` to do things, but they are not
callable as builtin methods on list object. you need to call like `filter(lambda x: x > 2, l)` and this is not chainable
I can flexible to call functions in chainable fashion like `l.filter(lambda x: x < 2).transform(lambda x: x ** 2).to_set(condition=lambda x: x < 100, cast=str)`
