def gcd(a, b):
  if (b==0):
    return a
  return gcd(b, a%b)


while True:
  dividend = int(input('DIVIDEND: '))
  divisor = int(input('DIVISOR: '))
  if divisor!=0:
    break
  print('INVALID. TRY AGAIN. \n')

print('GCD: ', str(gcd(dividend, divisor)))
