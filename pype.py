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


