def swapNum(x, y):
  return y, x

  
def swap2(a, b):
    if a > b:
        swap = a  # classic swap technique
        a = b
        b = swap
    return a, b
def driver():
  num1 = int(input("Input a number"))
  num2 = int(input("Input another number"))
  swap2(num1, num2)
  print(swapNum(num1,num2))