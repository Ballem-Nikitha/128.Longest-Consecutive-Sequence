class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        numset=set(nums)
        maxnum=0
        
        for num in numset:
            if num-1 not in numset:
                curr=num
                count=1
                while curr+1 in numset:
                    curr+=1
                    count+=1
                maxnum=max(maxnum,count)
        return maxnum