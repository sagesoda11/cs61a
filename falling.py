def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    product = 1
    if k == 0:
      print(1)
    for i in range(1,k+1):
      product = product*(n-i+1)
      i += 1
    print(product)
