class NegativeNumberError(Exception):
    pass

try:
    n = int(input('Enter a numerator: '))
    d = int(input('Enter a denominator: '))

    if n < 0 or d < 0:
        raise NegativeNumberError('Must be positive integers')

    q = n / d # Exception was raised when trying to divide by zero

    print(q)

except ZeroDivisionError:
    print('Denominator cannot be zero')

except ValueError:
    print('Inputs must be postitive numbers')

except NegativeNumberError:
    print('Inputs must be positive numbers')

except Exception as e:
    print('Something went wrong')
    print(e)