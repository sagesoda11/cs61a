def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    divisor = n
    while divisor >= 1:
      if n % divisor == 0:
        print(divisor)
      divisor -= 1

num = int(input("Enter a number: "))
factors(num)
