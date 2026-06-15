class Solution:
    def isHappy(self, n: int, seen: set = None) -> bool:
        if seen is None:
            seen = set()
        tempstr = str(n)
        sm = 0
        

        for i in range(len(tempstr)):
            sm += int(tempstr[i]) ** 2

        if sm == 1:
            return True

        if sm not in seen:
            seen.add(sm)
            return self.isHappy(sm, seen)
            
        return False



        

        
        
        
        
        