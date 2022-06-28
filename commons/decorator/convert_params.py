from functools import wraps

import flask


def convert_params(**request_type):
    fields = {key: value for key, value in request_type.items()}

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            kwargs = flask.request.args.to_dict()
            for k, v in kwargs.items():
                if fields[k] == "array":
                    kwargs[k] = v.split(",")
                elif fields[k] == "integer":
                    kwargs[k] = int(v)
                elif fields[k] == "boolean":
                    kwargs[k] = bool(int(v))
                elif fields[k] == "intarray":
                    kwargs[k] = v.split(",")
                    kwargs[k] = list(map(int, kwargs[k]))
                elif fields[k] == "floatarray":
                    kwargs[k] = v.split(",")
                    kwargs[k] = list(map(float, kwargs[k]))
            return f(*args, **kwargs)

        return wrapper

    return decorator
