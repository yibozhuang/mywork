def dfs(p, process_list, spaces):
    print("{}{} - {}".format(spaces * " ", p[0], p[2]))

    for proc in process_list:
        if proc[1] == p[0]:
            dfs(proc, process_list, (spaces+2))


def process_foreast(process_list):
    for p in process_list:
        if p[1] is not None:
            continue
        else:
            dfs(p, process_list, 0)


process_list = [
[5, 3, 'abc'],
[4, 3, 'ced'],
[9, 5, 'bcdh'],
[8, 5, 'dcf'],
[7, 4, 'cbmk'],
[6, 3, 'dkkj]'],
[3, 2, 'cd'],
[2, 1, 'fnc'],
[1, None, '67d'],
[21, None, '8h6'],
[22, 21, '908'],
[23, 21, 'ewet'],
[24, 22, 'kjet'],
[25, 22, 'k09t'],
[26, 23, 'kfkljsn'],
[27, 26, '9bdsn'],
[28, 24, 'k3jsn'],
]

process_foreast(process_list)
