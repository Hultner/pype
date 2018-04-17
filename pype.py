"""Pype, python pipelines

Author: Alexander Hultnér

The idea is to allow for pipestyle programming in python eg.
p(
  [1,2,3]
  | lambda x: x*2
  | sum
)
> 12

Roadmap:
    [x] Basic PoC using commas instead of pipes
    [ ] Use introspection to allow usage with the "|" pipe character
    [ ] Add generative testing using hypothesis
    [ ] Set up static analysis and automatic testing (travis and codeclimate)

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


