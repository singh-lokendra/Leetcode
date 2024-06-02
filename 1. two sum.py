from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx in range(len(nums)):
            current_num = nums[idx]
            diff = target - current_num

            if diff in visited:
                return sorted([idx, visited[diff]])

            visited[current_num] = idx

        return [-1, -1]
