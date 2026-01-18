# import the fizzbuzz function from the fizzbuzz script 

from fizzbuzz import fizzbuzz
import pytest


# start putting the tests into functions 


#test the function exists 

def test_fizzbuzz_exists():
    from fizzbuzz import fizzbuzz
    assert callable(fizzbuzz)

# test the basic functionality of the fizzbuzz function 


def test_fizzbuzz_basics():
    assert fizzbuzz(5) == [1,2,"fizz",4,"buzz"]


# test the 0 error

def test_fizzbuzz_zero_error():
    #import pytest 
    with pytest.raises(ValueError):
        fizzbuzz(0)

# test the negative value error

def test_fizzbuzz_negative():
    #import pytest
    with pytest.raises(ValueError):
        fizzbuzz(-1)

# test the error for the data type of num_entry 

def test_fizzbuzz_type():
    #import pytest
    with pytest.raises(TypeError):
        fizzbuzz("hello!")
