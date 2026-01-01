class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            seen[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if diff in seen:
                index = seen[diff]
                if index != i:
                    return [i, index]

        return []
        