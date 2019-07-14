def twoSum(nums, target):
    s = {}
    for i in range(len(nums)):
        k = target - nums[i]
        if k in s:
            m = s[k]
            return [m, i]
        else:
            s[nums[i]] = i

print(twoSum([2, 7, 11, 15], 9))
