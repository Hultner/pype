"""Pype, python pipelines

Author: Alexander Hultnér

The idea is to allow for pipestyle programming in python eg.

>>> p(
...   [1,2,3]
...   | lambda x: x*2
...   | sum
... )
 12

Roadmap:
    [x] Basic PoC using commas instead of pipes
    [ ] Use introspection to allow usage with the "|" pipe character
    [ ] Set up proper python module with setup.py
    [ ] Add generative testing using hypothesis
    [ ] Set up static analysis and automatic testing (travis and codeclimate)
    [ ] Publish to pypi
    [ ] Write a short article on the project and how it can be used

"""
from typing import Callable, Any


# def pipe(in_: t1, *args: Callable[[t1], tr]) -> tr:


def pipe(in_: Any, *args: Callable[[Any], Any]) -> Any:
    """Basic pipe functionality

    Example usage:
    >>> pipe(
    ...   [True, False, 1, 3],
    ...   all,
    ...   lambda x: "It's true" if x else "They lie"
    ... )
    'They lie'

    """
    for function in args:
        in_ = function(in_)

    return in_


