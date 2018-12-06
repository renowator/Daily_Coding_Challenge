def solution( args ):
    rev_number_list = []
    num = args[0]
    base = 10
    if len(args) > 1:
        base = args[1]
    if num < base:
        return True
    while num >= base:
        rev_number_list.append(num % base)
        num = num // base
    rev_number_list.append(num)
    for i in range(int(len(rev_number_list)/2)):
        if rev_number_list[len(rev_number_list) - 1 - i] != rev_number_list[i]:
            return False
    return True
