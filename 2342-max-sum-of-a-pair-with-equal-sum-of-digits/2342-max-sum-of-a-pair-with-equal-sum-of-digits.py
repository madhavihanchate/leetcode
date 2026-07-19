class Solution:
    def maximumSum(self, nums):
        mp = {}
        ans = -1
        for num in nums:
            x = num
            digit_sum = 0
            while x:
                digit_sum += x % 10
                x //= 10
            if digit_sum in mp:
                ans = max(ans, num + mp[digit_sum])
                mp[digit_sum] = max(mp[digit_sum], num)
            else:
                mp[digit_sum] = num
        return ans
                
            
        