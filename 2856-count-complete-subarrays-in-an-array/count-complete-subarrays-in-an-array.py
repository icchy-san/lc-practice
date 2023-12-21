class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        kind_elems = len(set(nums))
        cnt = 0
        left = 0
        right = 0
        counter = Counter()

        # if right reaches length of n, it means that slider looks all elements.
        while right < n:
            # sliding window
            # left <-> right
            counter[nums[right]] += 1
            while len(counter) == kind_elems:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                cnt += n - right
            right += 1

        return cnt