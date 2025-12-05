#create a function for fizzbuzz

#define the function 
def fizzbuzz(num_entry):

    # create checks to ensure that num_entry is valid 

    #check if num_entry is numeric or integer 
# if num_entrey isnt numeric
    if not isinstance(num_entry, int):
        # then give this error message
        raise TypeError("num_entry must be an integer")
    
    # if num_entry is 0

    if num_entry == 0 :
        # then give this error msg
        raise ValueError ("num_entry must be bigger than 0")
    
    # if num_entry is negative 

    if num_entry < 0:
        raise ValueError("num_entry must not be negative")
    
    #start an empty list 

    results = []

    # start a for loop for the fizzbuzz problem 

    for x in range ( 1, num_entry+1):

        # if x is a multiple of 3 AND 5 then 

        if x % 3 == 0 and x % 5 == 0:
            #append fizzbuzz to the list 
            results.append("fizzbuzz")
        #  if the x is a multiple of 3 then 
        elif x % 3 == 0:
            #append fizz to the list
            results.append("fizz")

        # if the x is a multiple of 5 

        elif x % 5 == 0: 
            # append buzz to the list
            results.append("buzz")
        
        # if none of those conditions are met then

        else: 
            results.append(x)

        # return the result list 

    return results


print(fizzbuzz(10))