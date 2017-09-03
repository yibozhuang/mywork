def circularPrint(matrix):
  m = len(matrix)
  n = len(matrix[0])
  k = 0
  l = 0

  while (k < m and l < n):
    # print first row
    for i in range(l, n):
      print str(matrix[k][i])+" "
    k += 1

    # print vertical down
    for i in range(k, m):
      print str(matrix[i][n-1])+" "
    n -= 1

    # print backwards
    if (k < m):
      for i in range(n-1, l-1, -1):
        print str(matrix[m-1][i]) + " "
      m -= 1

    # print upwards
    if (l < n):
      for i in range(m-1, k-1, -1):
        print str(matrix[i][l]) + " "
      l += 1


matrix = [  [1, 3, 5], [2, 4, 6], [7, 9, 11], [8, 10, 12], [13, 15, 17] ]

circularPrint(matrix)

