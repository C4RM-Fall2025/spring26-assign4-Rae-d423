def FizzBuzz(start, finish):
    outlist = []
    # Loop through the numbers from start to finish (inclusive)
    for i in range(start, finish + 1):
        # Check if the number is divisible by both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")
        # Check if divisible by 3
        elif i % 3 == 0:
            outlist.append("fizz")
        # Check if divisible by 5
        elif i % 5 == 0:
            outlist.append("buzz")
        # If none of the above, append the number itself
        else:
            outlist.append(i)
            
    return outlist
