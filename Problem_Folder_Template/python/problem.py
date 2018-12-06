class Problem:
    def __init__(self):
        self.fn = lambda x: None

    def getSolution(self, solution):
        self.fn = solution

    def solve(self, args):
        return self.fn(args)





