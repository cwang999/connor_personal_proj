num1 = int(input("Input a number"))
num2 = int(input("Input another number"))
def swapNum(x, y):
  return num2, num1
print(swapNum(num1,num2))
  
def swap2(a, b):
    if a > b:
        swap = a  # classic swap technique
        a = b
        b = swap
    return a, b
