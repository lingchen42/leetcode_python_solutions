class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        count_seq = [1, 1]
        for num in range(2, n):    
            t_count_seq = []
            count = 1
            for i, v in enumerate(count_seq[:-1]):
                if count_seq[i+1] == v:
                    count += 1
                else:
                    t_count_seq.extend([count, v])
                    count = 1   
            if count_seq[-1] == v:
                t_count_seq.extend([count, v])
            else:
                t_count_seq.extend([1, count_seq[-1] ])
            count_seq = t_count_seq
        count_seq = [str(i) for i in count_seq]
                
        return "".join(count_seq)