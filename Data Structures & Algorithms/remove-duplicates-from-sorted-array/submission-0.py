class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = sorted(set(nums))
        nums[:len(nums1)] = nums1
        return len(nums1)