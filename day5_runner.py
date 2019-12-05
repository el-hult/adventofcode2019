import io
from contextlib import redirect_stdout

from computer import get_test_program, Computer
from util import manage_input

if __name__ == "__main__":
    p = get_test_program()
    c = Computer(p)
    f = io.StringIO()
    with manage_input([1]):
        with redirect_stdout(f):
            c.run_until_stop()
    outputs = [int(i) for i in f.getvalue().split()]

    print(f"Ans A:{outputs[-1]}")