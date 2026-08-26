from hello import add


def test_add():
    assert (add(1, 1)) == 3


from hello import random_hash


def test_random_hash():
    result = random_hash()
    assert isinstance(result, str)
    assert len(result) == 64
