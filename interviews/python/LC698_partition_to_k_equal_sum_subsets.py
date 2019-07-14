def dfs(index, nums, k, bucket, equal_sum):
    if index == len(nums):
        return len(set(bucket)) == 1

    for i in range(k):
        bucket[i] += nums[index]
        if bucket[i] <= equal_sum and dfs(index+1, nums, k, bucket, equal_sum):
            return True

        bucket[i] -= nums[index]
        if bucket[i] == 0:
            break

    return False

def canPartitionKSubsets(nums, k):
    nums.sort(reverse=True)

    bucket = [0] * k
    equal_sum = sum(nums) // k

    return dfs(0, nums, k, bucket, equal_sum)

print(canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
