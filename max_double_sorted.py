def sort_double(nums):
    if len(nums)==1:
        return nums[0]
    first = nums[0]
    mid = nums[len(nums)//2]
    last = nums[-1]
    if mid>first:
       return sort_double(nums[len(nums)//2:])
    else:
       return sort_double(nums[:len(nums)//2])

print(sort_double([2,3,3,3,4,2]))
