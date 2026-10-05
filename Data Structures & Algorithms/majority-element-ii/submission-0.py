class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        
        for num in set(nums):   
            count = 0
            for x in nums:
                if x == num:
                    count += 1
            if count > n // 3:
                result.append(num)
        
        return result