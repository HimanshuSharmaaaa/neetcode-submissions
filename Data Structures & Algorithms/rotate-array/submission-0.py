class Solution:
   def rotate(self, nums: List[int], k: int) -> None:
     
        k %= len(nums)
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last) 
        