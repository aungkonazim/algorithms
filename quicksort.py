def pivot_subroutine(nums):
    pivot = nums[0]
    i = 1
    for j in range(1,len(nums)):
        if nums[j]<nums[0]:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i+=1
    temp = nums[i-1]
    nums[i-1] = nums[0]
    nums[0] = temp
    return nums,i-1

def quicksort(nums):
    if len(nums)<=1:
        return nums
    else:
        nums,index = pivot_subroutine(nums)
        leftnums = quicksort(nums[:index])
        rightnums = quicksort(nums[(index+1):])
        return leftnums+[nums[index]]+rightnums

print(quicksort([8,5,1,3,4,3]))

