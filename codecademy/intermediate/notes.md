# Additional Notes



## Function Annotations

### What are function annotations?

Function annotations are a way to add arbitrary metadata to function parameters and return values. They are stored in the function’s `__annotations__` attribute as a dictionary and have no effect on any other part of the function.

### How do I use function annotations?

Function annotations are created by placing a colon after the parameter name or return value followed by an expression evaluating to the value of the annotation. Multiple annotations are separated by commas.

```python
def func(param1: expression1, param2: expression2) -> expression3:
    pass
```

The function above has two parameters, `param1` and `param2`, and a return value, `expression3`.

`param1`’s annotation is `expression1`, and `param2`’s annotation is `expression2`. `expression3` is the annotation for the return value.

### What are function annotations used for?

Function annotations are used to provide type hints to static type checkers and IDEs. They can also be used by decorators to modify the behavior of a function.

```python
def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
    pass
```

would result in an __annotations__ dictionary that looks like this:

```python
{
    'a': 'x',
    'b': 11,
    'c': list,
    'return': 9
}
```

## Hinting Types

### What are type hints?

Type hints are a way to specify the expected type of a value in Python. They are not enforced by the interpreter, but they can be used by static type checkers to verify that your code is type safe.

### How do I use type hints?

Type hints are created by placing a colon after the parameter name or return value followed by the type of the value. Multiple type hints are separated by commas.

```python
def person(name: str, age: int) -> str:
    return f"{name} is a {age} year old programmer"
```

### Whats the difference between type hints and function annotations?

Function annotations are a way to add arbitrary metadata to function parameters and return values. They are stored in the function’s `__annotations__` attribute as a dictionary and have no effect on any other part of the function.

Type hints are a way to specify the expected type of a value in Python. They are not enforced by the interpreter, but they can be used by static type checkers to verify that your code is type safe.

