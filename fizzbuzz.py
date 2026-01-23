def fizzbuzz(n):

    #negative value check

    if n <0:
        raise ValueError("Input must be a non negative number")


    if n % 15 == 0: 
        return "Fizzbuzz"
    
    if n % 3 == 0: 
        return "Fizz"
    if n % 5 == 0: 
        return "Buzz"
    


    #return the input as strings
    return str(n)