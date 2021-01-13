import math
def rotated_search(nums,start,end,target):
    print(start,end,'s')
    if end<=start:
        if nums[start]==target:
            return start
        else:
            return -1
    mid = math.floor((start+end)/2)
    if nums[mid]==target:
        return mid
    if nums[start]<nums[mid] and nums[start]<=target<nums[mid]:
        return rotated_search(nums,start,mid,target)
    return rotated_search(nums,mid+1,end,target)

nums = [4,4,5,5,6,7,8,9,0,1,2,3]
for i in range(1):
    print(rotated_search(nums,0,len(nums),5),5
          )

import math
print(math.inf)