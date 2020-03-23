from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    src = [set() for _ in range(numCourses)]
    dst = [set() for _ in range(numCourses)]

    for d, s in prerequisites:
        src[d].add(s)
        dst[s].add(d)

    ans = [x for x in range(numCourses) if not src[x]]

    for s in ans:
        for d in dst[s]:
            src[d].remove(s)

            if not src[d]:
                ans.append(d)

    return ans if len(ans) == numCourses else []


print(findOrder(2, [[1, 0]]))
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
