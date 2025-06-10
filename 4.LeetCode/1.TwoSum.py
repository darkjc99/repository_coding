from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    values = []
    if 2 <= len(nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # if nums[i] + nums[j] == target:
                values.append([i, j])
        return values
    return []


nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)
