import problem
from types import *


class Test:
    def __init__(self):
        self.test_result = []
        self.grade = ""

    def test_template(self, prob):
        self.sample_test1(prob)
        self.sample_test2(prob)
        tests_passed = 0
        for i in range(len(self.test_result)):
            if test.test_result[i]:
                tests_passed += 1
        score = str(tests_passed*100/len(self.test_result))
        self.grade += score + "%"
        return "Number of tests passed: {}\nNumber of tests failed: {}\nScore: {}".format(tests_passed, len(self.test_result) - tests_passed, self.grade)

    def sample_test1(self, prob):
        try:
            assert type(prob.problem_template([" "])) is StringType, "Not a valid problem output: %s" % problem
            print("sample_test1:PASSED")
            self.test_result.append(True)
        except AssertionError as e:
            print (e.args[0])
            print("sample_test1:FAILED")
            self.test_result.append(False)

    def sample_test2(self,prob):
        try:
            assert prob.problem_template([]) == "hello world: ", "The derived result does not match: '%s' vs. '%s'" % (prob.problem_template([]), "hello world: ")
            assert prob.problem_template(["b"]) == "hello world: b", "The derived result does not match: '%s' vs. '%s'" % (prob.problem_template([""]), "hello world: b")
            assert prob.problem_template(["a"]) == "hello world: a", "The derived result does not match: '%s' vs. '%s'" % (prob.problem_template(["a"]), "hello world: a")
            print("sample_test2:PASSED")
            self.test_result.append(True)
        except AssertionError as e:
            print (e.args[0])
            print("sample_test2:FAILED")
            self.test_result.append(False)


if __name__ == "__main__":
    test = Test()
    prob = problem.Problem()
    print(test.test_template(prob))