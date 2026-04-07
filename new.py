import unittest 

class calculator:
    def substraction(self,a, b):
        return a-b
    
class  test(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()
    
    def test_substraction(self):
        self.assertEqual(self.calc.substraction(1,1),0)
        
        
        
if __name__ == "__main__":
    unittest.main()