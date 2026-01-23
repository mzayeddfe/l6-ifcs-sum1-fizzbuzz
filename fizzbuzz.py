def fizzbuzz(n):

    if n % 15 == 0: 
        return "Fizzbuzz"
    
    if n % 3 == 0: 
        return "Fizz"
    if n % 5 == 0: 
        return "Buzz"
    


    #return the input as strings
    return str(n)