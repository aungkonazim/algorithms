def pivot_subroutine(nums):
    i = 1
    for j in range(1,len(nums)):
        if nums[j]>nums[0]:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i+=1
    temp = nums[i-1]
    nums[i-1] = nums[0]
    nums[0] = temp
    return nums,i-1

def kthsmallest(nums,k):
    if len(nums)==1:
        return nums[0]
    nums,k_1 = pivot_subroutine(nums)
    if k_1+1==k:
        return nums[k_1]
    elif k_1+1<k:
        return kthsmallest(nums[(k_1+1):],k-k_1-1)
    else:
        return kthsmallest(nums[:k_1],k)

print(kthsmallest([0,0,4,3,5,5,1],3))
