import math
def abundant(n):
  divisor = 1
  sum = 0
  while divisor <= n:
    if n % divisor == 0:
      if divisor <= math.sqrt(n):
        print(str(divisor) + "*" + str(int(n/divisor)))
      sum += divisor
    divisor += 1
  print(sum-n > n)

abundant(361)
