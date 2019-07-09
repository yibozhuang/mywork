def splitEqualSum(array):
    n = len(array)
    error = "cannot split"

    if n == 0:
        print(error)
        return

    s = sum(array)
    if (s % 2 != 0):
        print(error)
        return

    l = 0
    r = n-1

    left_sum = 0
    right_sum = 0

    while l <= r:
        if left_sum > right_sum:
            right_sum += array[r]
            r-= 1

        else:
            left_sum += array[l]
            l+= 1

    if left_sum == right_sum:
        print(array[:l])
        print(array[r+1:])

    else:
        print(error)

    return


splitEqualSum([1,2,1,1,3])
splitEqualSum([1,1,1,1,1,5])
splitEqualSum([5,2,3])
splitEqualSum([5,2,3,7])
