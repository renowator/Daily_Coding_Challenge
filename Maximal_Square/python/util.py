class Problem:
    def __init__(self):
        self.fn = lambda x: None

    def getSolution(self, solution):
        self.fn = solution

    def solve(self, args):
        return self.fn(args)


class Test:
    def __init__(self, problem):
        self.test_result = []
        self.grade = ""
        self.pr = problem

    def run_tests(self, i_o_dict):
            for in_val in i_o_dict:
                try:
                    assert self.pr.solve(in_val) == i_o_dict[in_val], "Error"
                    self.test_result.append(True)
                except AssertionError:
                    self.test_result.append(False)
            return self.test_result

    def test_run(self, i_o_dict):
        if type(i_o_dict) is None:
            return None
        tests_passed = 0
        self.test_result = self.run_tests(i_o_dict)
        for i in range(len(self.test_result)):
            if self.test_result[i]:
                tests_passed += 1
        score = str(tests_passed*100/len(self.test_result))
        self.grade += score + "%"
        return "Number of tests passed: {}\nNumber of tests failed: {}\nScore: {}".format(tests_passed, len(self.test_result) - tests_passed, self.grade)


