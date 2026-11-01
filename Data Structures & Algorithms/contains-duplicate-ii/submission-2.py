class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       n=len(nums)
       last={}
       for i in range(n):
        
            if nums[i] in last and i-last[nums[i]]<=k:
                return True
            last[nums[i]]=i    
       return False         
        
        