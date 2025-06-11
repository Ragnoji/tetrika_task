from inspect import signature

def strict(func):
    def wrapper(*args):
        pos_args = len(signature(func).parameters)

        if pos_args != len(args):
            raise TypeError(f"{func.__name__}() takes {pos_args} positional arguments "
                            f"but {len(args)} were given")

        for i, param in enumerate(signature(func).parameters.keys()):
            req_type = func.__annotations__.get(param, None)
            if req_type is not None and not isinstance(args[i], req_type):
                raise TypeError(f"Unexpected type of positional argument at index {i}")
        res = func(*args)

        return_type = func.__annotations__.get('return', None)
        if return_type is not None and not isinstance(res, return_type):
            raise TypeError("Returned value's type is different from expected")
        return res

    return wrapper
