import sys
sys.path.append('../..')

from util import *
from solution import solution

prob = Problem()
prob.getSolution(solution)
test = Test(prob)
i_o_vals = {("!","b"):"hello world: !b", "ad da": "hello world: ad da", ("1","2","3"):"hello world: 123"}
print(test.test_run(i_o_vals))