#
# Problem: 762. Prime Number of Set Bits in Binary Representation
# Difficulty: Easy
# Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-21
# Language: python3
# Date: 2026-02-21


#try dp method

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def isPrime(num, divisor=2):
            #base cases
            if num<2:
                return False
            if divisor*divisor>num:
                #divisor>=num
                return True
                
            if num%divisor==0:
                return False


            return isPrime(num,divisor+1)

        return sum(isPrime(bin(num).count('1')) for num in range(left,right+1))

        
        #sol 1: O(n) time & O(1) space

        def isPrime(num): #O(log right) time
            if num<2:
                return False
            if num==2:
                return True
            
            for i in range(2,num-1):
                if num%i==0:
                    return False

            return True

        return sum(isPrime(bin(num).count('1')) for num in range(left,right+1))
        
