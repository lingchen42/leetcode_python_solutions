class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        outlist = []
        
        for i in range(1, n+1):
            if i%3 == 0:
                if i%5 == 0:
                    outlist.append("FizzBuzz")
                else:
                    outlist.append("Fizz")
                    
            elif i%5 == 0:
                outlist.append("Buzz")
                
            else:
                outlist.append(str(i))
            
        return outlist 