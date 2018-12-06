from util import Problem, Test
from solution import solution
import random


def generate_palindrome_tests(len = 2, max_base = 10):
    i_o_dict = {}
    length = len
    for base in range(2,max_base):
        pal = 0
        for i in range(length // 2):
            # get random number within base
            num = random.randint(1, base - 1)
            pal += (base ** i) * num
            pal += (base ** (length - 1 - i)) * num
        i_o_dict[(pal, base)] = True
    for base in range(2, max_base):
        pal = 0
        for i in range(length // 2):
            # get random number within base
            num1 = random.randint(1, base - 1)
            num2 = random.randint(0,base-1)
            while num1 == num2:
                num2 = random.randint(0,base-1)
            pal += (base ** i) * num2
            pal += (base ** (length - 1 - i)) * num1
        i_o_dict[(pal, base)] = False
    return i_o_dict


prob = Problem()
prob.getSolution(solution)
test = Test(prob)
i_o_vals = generate_palindrome_tests(5)
print(test.test_run(i_o_vals))