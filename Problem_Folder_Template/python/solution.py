def solution(args = None):
    if args is None:
        return None
    retstr = "hello world: "
    for i in range(len(args)):
        retstr += args[i]
    return retstr
