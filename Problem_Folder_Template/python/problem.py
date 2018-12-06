class Problem:
    def problem_template(self, args):
        return self.hello_world(args)

    def hello_world(self, args):
        retstr = "hello world: "
        for i in range(len(args)):
            retstr += args[i]
        return retstr


