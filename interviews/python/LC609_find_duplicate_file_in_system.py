import collections

def findDuplicate(paths):
    M = collections.defaultdict(list)

    for line in paths:
        data = line.split()
        root = data[0]
        for file in data[1:]:
            name, _, content = file.partition('(')
            M[content[:-1]].append(root + '/' + name)

    return [x for x in M.values() if len(x) > 1]

input = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

print(findDuplicate(input))
