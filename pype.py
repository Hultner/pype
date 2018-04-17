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

def pipe(in_, *args: "Function"):
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


