class Solution(object):
    def findPeakElement(self, nums):
        l,r=0,len(nums)
        while l<=r:
            mid=(l+r)//2
            if mid==0:
                if mid+1==len(nums):
                    return mid
                else:
                    if nums[mid+1]<nums[mid]:
                        return mid
            else:
                if mid==len(nums)-1:
                    if mid-1>=0 and nums[mid-1]<nums[mid]:
                        return mid
                else:
                    if mid-1>=0 and mid+1<len(nums) and nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                        return mid
            if mid<len(nums)-1 and nums[mid+1]>=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1

        