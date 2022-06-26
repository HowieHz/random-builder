from . import do_random


def test_init():
    assert isinstance(do_random.name, str)
    assert isinstance(do_random.__all__, list)
    assert isinstance(do_random.__version__, str)
