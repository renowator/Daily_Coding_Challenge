import problem
from types import *


class Test:
    def __init__(self, problem):
        self.test_result = []
        self.grade = ""
        self.pr = problem

    def run_tests(self, i_o_dict):
        try:
            for in_val in i_o_dict:
                assert self.pr.solve(in_val) == i_o_dict[in_val], "Error"
                self.test_result.append(True)
        except(AssertionError):
            self.test_result.append(False)
        return self.test_result

    def test_run(self, i_o_dict):
        self.test_result = self.run_tests(i_o_dict)
        if type(i_o_dict) is None:
            return None
        tests_passed = 0
        for i in range(len(self.test_result)):
            if test.test_result[i]:
                tests_passed += 1
        score = str(tests_passed*100/len(self.test_result))
        self.grade += score + "%"
        return "Number of tests passed: {}\nNumber of tests failed: {}\nScore: {}".format(tests_passed, len(self.test_result) - tests_passed, self.grade)


def solution( args = None):
    if args is None:
        return None
    retstr = "hello world: "
    for i in range(len(args)):
        retstr += args[i]
    return retstr

if __name__ == "__main__":
    prob = problem.Problem()
    prob.getSolution(solution)
    test = Test(prob)
    i_o_vals = {("!","b"):"hello world: !b", "ad da": "hello world: ad da", ("1","2","3"):"hello world: 123"}
    print(test.test_run(i_o_vals))