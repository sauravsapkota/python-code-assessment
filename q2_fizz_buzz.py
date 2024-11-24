def fizz_buzz(n):
    result = []
    
    for i in range(1, n + 1):
        # Check for multiples of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Check for multiples of 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Check for multiples of 5
        elif i % 5 == 0:
            result.append("Buzz")
        # For all other numbers, add the number as a string
        else:
            result.append(str(i))
    
    return result

# Example usage
n = 15
print(fizz_buzz(n))
