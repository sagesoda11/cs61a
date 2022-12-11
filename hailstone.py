def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 1
    print(n)
    while n != 1:
      if n%2 == 0:
        n = int(n/2)
      else:
        n = 3*n + 1
      print(n)
      count += 1
    print("length = " + str(count)) #?

num = int(input("Enter a number: "))
   
hailstone(num)
