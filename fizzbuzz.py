def fizzbuzz(n):

    # check if value is bigger than 0 to disqualify negatives 

    if n < 0 :
        raise ValueError("Input must be a positive number")

    if n % 15 == 0: 
        return "Fizzbuzz"
    
    if n % 3 == 0: 
        return "Fizz"
    if n % 5 == 0: 
        return "Buzz"
    


    #return the input as strings
    return str(n)