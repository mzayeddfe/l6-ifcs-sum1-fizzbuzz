# import fizzbuzz

from fizzbuzz import fizzbuzz 
import pytest

# check the function returns numeric inputs as string

def test_return_as_string():
    assert fizzbuzz(1) == "1"

#test function works for multiples of 3

def test_multi_three():
    assert fizzbuzz(3) == "Fizz"


# test function works for multiples of 5 

def test_multi_five():
    assert fizzbuzz(5) == "Buzz"


# test function works for multiples of 15 

def test_multi_fifteen():
    assert fizzbuzz(15) == "Fizzbuzz"

# start testing for errors

#check that input is int
def test_non_int_input():
    with pytest.raises(TypeError):
        fizzbuzz("hello!")


def test_non_negative_input():
    with pytest.raises(ValueError):
        fizzbuzz(-1)