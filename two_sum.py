#! /usr/bin/python

from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        nums = sorted(nums, reverse = True)
        for i in range(len(nums)):
            if nums[i] > target:
                continue
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return sorted([indices[nums[i]], indices[nums[j]]])
                else:
                    j += 1

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        for i in range(len(nums)):
            summand = target - nums[i]
            if summand in indices.keys():
                if i != indices[summand]:
                    return [i, indices[summand]]
