def inc(x):
    if x is str:
        Exception("Not a number")
    return x + 1


def test_answer():
    assert inc(3) == 4
