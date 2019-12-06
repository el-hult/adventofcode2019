import io
from contextlib import redirect_stdout

from computer import get_day5_program, Computer
from util import manage_input

if __name__ == "__main__":
    p = get_day5_program()
    c = Computer(p)
    f = io.StringIO()
    with manage_input([1]):
        with redirect_stdout(f):
            c.run_until_stop()
    outputs = [int(i) for i in f.getvalue().split()]
    print(f"Ans A:{outputs[-1]}")

    c = Computer(p)
    f = io.StringIO()
    with manage_input([5]):
        with redirect_stdout(f):
            c.run_until_stop()
    outputs = [int(i) for i in f.getvalue().split()]
    print(f"Ans B:{outputs[-1]}")