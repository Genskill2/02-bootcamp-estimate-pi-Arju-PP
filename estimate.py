import math
import unittest
def wallis(n):
	pi=1
	for i in range(1,n+1):
		pi=pi*((4)*(i**2))/(((4)*(i**2))-1)
	
	return 2*pi

def distance(x,y):
	import math
	
	dist= math.sqrt((x**2)+(y**2))
	return dist

def monte_carlo(num):
	incircle=0
	total=0

	import random 
	for i in range(1,num+1):
		x=random.random()
		y=random.random()
		x=x*2-1
		y=y*2-1
		if distance(x,y) <1 :
			incircle+=1
		total+=1
		
	pi=4*incircle/total
	return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
