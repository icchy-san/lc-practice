class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # To calculate distance in each element, sorting is useful.
        nums.sort()
        
        # result array
        res = []

        # Array size is 3.
        for i in range(0, len(nums), 3):
            if k < nums[i+2] - nums[i]:
                return []
            res.append(nums[i:i+3])

        return res