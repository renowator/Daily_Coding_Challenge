import sys
sys.path.append('../..')

from util import *
from solution import solution

prob = Problem()
prob.getSolution(solution)
test = Test(prob)
i_o_dict = {((0,1,1,1), (1, 1,1,1), (1,1,1,1), (1,1,1,1)): 9, ((0, 1),(1, 0)):1, ((0,1,1,1),(1,1,0,1),(0,1,1,1)):1}
print(test.test_run(i_o_dict))
