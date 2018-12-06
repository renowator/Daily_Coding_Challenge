import problem
import random
from types import *


class Test:
    def __init__(self):
        self.test_result = []
        self.grade = ""

    def test_template(self, prob):
        self.sample_test1(prob)
        self.sample_test2(prob)
        self.sample_test3(prob)
        self.sample_test4(prob)
        tests_passed = 0
        for i in range(len(self.test_result)):
            if test.test_result[i]:
                tests_passed += 1
        score = str(tests_passed * 100 / len(self.test_result))
        self.grade += score + "%"
        return "Number of tests passed: {}\nNumber of tests failed: {}\nScore: {}".format(tests_passed, len(
            self.test_result) - tests_passed, self.grade)

    def sample_test1(self, prob):
        try:
            assert type(prob.problem_template([1231])) is bool, "Not a valid problem output: %s" % problem
            print("sample_test1:PASSED")
            self.test_result.append(True)
        except AssertionError as e:
            print(e.args[0])
            print("sample_test1:FAILED")
            self.test_result.append(False)

    def sample_test2(self, prob):
        try:
            assert prob.problem_template([1]) == True, "The derived result does not match: 1 '%s' vs. '%s'" % (
            prob.problem_template([]), True)
            assert prob.problem_template([998]) == False, "The derived result does not match: 100 '%s' vs. '%s'" % (
            prob.problem_template([998]), False)
            assert prob.problem_template(
                [1001001]) == True, "The derived result does not match: 1001001 '%s' vs. '%s'" % (
            prob.problem_template([1001001]), True)
            print("sample_test2:PASSED")
            self.test_result.append(True)
        except AssertionError as e:
            print(e.args[0])
            print("sample_test2:FAILED")
            self.test_result.append(False)

    def sample_test3(self, prob):
        try:
            assert prob.problem_template([10]) == False, "The derived result does not match: 10 '%s' vs. '%s'" % (
            prob.problem_template([12312114]), True)
            assert prob.problem_template([123456789876543210]) == False, "The derived result does not match: 123456789876543210 '%s' vs. '%s'" % (prob.problem_template([123456789876543210]), False)
            assert prob.problem_template([1001001001]) == True, "The derived result does not match: 1001001001 '%s' vs. '%s'" % (prob.problem_template([1001001001]), True)
            print("sample_test3:PASSED")
            self.test_result.append(True)
        except AssertionError as e:
            print(e.args[0])
            print("sample_test3:FAILED")
            self.test_result.append(False)

    def sample_test4(self, prob):
        try:
            for base in range(2, 10):
                for i in range(100):
                    pal = generate_palindrome(base)
                    assert prob.problem_template([pal, base]) == True, "Palindrome test failed %d with base %d" % (pal, base)
            self.test_result.append(True)
            print("sample_test4:PASSED")
        except AssertionError as e:
            print(e.args[0])
            print("sample_test4:FAILED")
            self.test_result.append(False)

def generate_palindrome(base):
    length = random.randint(1, 5)
    pal = 0
    for i in range(length // 2):  
        # get random number within base
        num = random.randint(1, base - 1)
        pal += (base ** i) * num
        pal += (base ** (length - 1 - i)) * num
    return pal


if __name__ == "__main__":
    test = Test()
    prob = problem.Problem()
    print(test.test_template(prob))
