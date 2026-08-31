from hello import random_hash


def test_random_hash():
    result = random_hash()
    assert isinstance(result, str)
    assert len(result) == 64
