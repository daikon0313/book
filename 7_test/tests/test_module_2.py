from src.module_2 import sub_numbers

def test_sub_numbers_1():
    assert sub_numbers(2,1) == 1

def test_sub_numbers_2():
    assert sub_numbers(-1,-2) == -3