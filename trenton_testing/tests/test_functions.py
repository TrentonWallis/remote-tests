import trenton_testing.hw as hw  #Is there a way to make this more general?

def test_hw_func1():
    x = 5 
    y = 7
    assert hw.add(x, y) == 12

def test_hw_func2():
    a = 3
    b = 6
    assert hw.sub(a, b) == -3
    