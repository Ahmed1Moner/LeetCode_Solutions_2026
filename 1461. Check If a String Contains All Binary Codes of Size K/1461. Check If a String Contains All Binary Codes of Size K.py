#
# Problem: 1461. Check If a String Contains All Binary Codes of Size K
# Difficulty: Medium
# Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/?envType=daily-question&envId=2026-02-23
# Language: python3
# Date: 2026-02-23


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        #sol 2: O(n*k) time & O(k*2^k) space

        seen=set()
        size,codes=len(s),2**k

        for i in range(size-k+1):
            seen.add(s[i:i+k]) #O(k) time & O(k*2^k) space

            if len(seen)==codes:
                return True
        return False


        #sol 1: brute force TLE: O(2^k*(n+k)) time & O(2^k*k) space
        #(k=30 →1 billion strings💀)

        codes = [format(i,f'0{k}b') for i in range(2**k)]

        # codes = [''.join(bit) for bit in product('01',repeat=k)] #O(2^k*k) time & O(2^k*k) space

        return all(code in s for code in codes) #O(n*2^k) time
        
