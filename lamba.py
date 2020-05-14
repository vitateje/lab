import unittest


def my_function(input):
  return 5

class TestClass(unittest.TestCase):
 def my_test(self):
    self.assertEqual(my_function(1), 5) #checking 1 becomes 0



#soma

soma = lambda x,y : x + y


print(soma(9,10))