#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        c = fct(*args)
    except ValueError as ve:
        print("Exception:", ve, file=sys.stderr)
        return (None)
    except TypeError as te:
        print("Exception:", te, file=sys.stderr)
        return (None)
    except ZeroDivisionError as zd:
        print("Exception:", zd, file=sys.stderr)
        return (None)
    except IndexError as ie:
        print("Exception:", ie, file=sys.stderr)
        return (None)
    return (c)
