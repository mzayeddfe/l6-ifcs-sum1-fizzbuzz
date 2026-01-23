# import fizzbuzz

from fizzbuzz import fizzbuzz 

# check the function returns numeric inputs as string

def test_return_as_string():
    assert fizzbuzz(1) == "1"

#test function works for multiples of 3

def test_multi_three():
    assert fizzbuzz(3) == "Fizz"