def waterTrap(towerList):
  size = len(towerList)
  
  left = [0 for x in range(size)]
  right = [0 for x in range(size)]

  water = 0

  left[0] = towerList[0]
  for i in range (1, size):
    left[i] = max(left[i-1], towerList[i])

  right[size-1] = towerList[size-1]
  for i in range(size-2, -1, -1):
    right[i] = max(right[i+1], towerList[i])

  for i in range(size):
    water += min(left[i], right[i]) - towerList[i]

  return water


tower = [3, 0, 0, 2, 0, 4]
tower2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print waterTrap(tower)
print waterTrap(tower2)
