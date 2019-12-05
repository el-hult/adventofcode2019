from util import manage_input

def test_some():
    with manage_input([123,"hej","oops"]):
        assert input("boo") == 123
        assert input() == "hej"
        assert input("") == "oops"
