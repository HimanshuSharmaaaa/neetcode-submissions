class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
      people.sort()  
      B=0
      n=len(people)

      l,r=0,n-1

      while l<=r:
        B+=1
        addition=people[l]+people[r]
        if addition<=limit:
            l+=1
        r-=1

      return B  