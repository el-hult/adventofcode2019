import builtins
from contextlib import contextmanager


@contextmanager
def manage_input(list_of_strings_to_give_as_input):
    t = builtins.input
    g = (x for x in list_of_strings_to_give_as_input)
    def my_input(*args):
        return next(g)
    builtins.input = my_input
    yield
    builtins.input = t