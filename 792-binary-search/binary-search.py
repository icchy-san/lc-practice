class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        
        return self.recursive_search(0, len(nums)-1)
        
    def recursive_search(self, left: int, right: int) -> int:
        if left > right:
            return -1
        middle_point = (left + right) // 2

        if self.target == self.nums[middle_point]:
            return middle_point
        elif self.target < self.nums[middle_point]:
            return self.recursive_search(left, middle_point-1)
        else:
            return self.recursive_search(middle_point+1, right)

