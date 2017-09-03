def getMaxSum(array):
  max = 0
  sum = 0

  for i in range(len(array)):
    sum += array[i]
    if (max < sum):
      max = sum
    elif (sum < 0):
      sum = 0

  return max

array = [-8, 3, -2, 4, -10]
print getMaxSum(array)
