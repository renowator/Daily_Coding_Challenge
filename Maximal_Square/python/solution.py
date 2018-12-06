def solution(args = None):
    if args is None:
        return None
    input_list = list(args)
    collen = len(input_list)
    rowlen = len(input_list[0])
    max_square = 0
    for i in range(collen):
        for j in range(rowlen):
            curr_square = 0
            test = input_list[i][j] == 1
            while test:
                curr_square += 1
                if i+curr_square < collen and j+curr_square < rowlen:
                    for colindex in range(i, i+curr_square):
                        if input_list[colindex][j+curr_square] == 0:
                            test = False
                    for rowindex in range(j, j+curr_square):
                        if input_list[i+curr_square][rowindex] == 0:
                            test = False
                    if input_list[i+curr_square][j+curr_square] == 0:
                        test = False
                else:
                    test = False
            max_square = max(max_square,curr_square*curr_square)
    return max_square


