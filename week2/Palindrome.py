import re

class Palindrome:
  def __call__(self, string):
    string = string.lower()
    string = re.sub(r"[^a-z]", "", string)
    return string == string[::-1]

def tester():
  palindrometest = Palindrome()
  while True:
    x = input("Enter a string: ")
    print(f"Is the string you entered a palindrome? The test says: {palindrometest(x)}")

tester()
