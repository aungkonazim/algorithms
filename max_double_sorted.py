# You are a given a unimodal array of n distinct elements,
# meaning that its entries are in increasing order up until its maximum element,
# after which its elements are in decreasing order.
# Give an algorithm to compute the maximum element that runs in O(log n) time.

def sort_double(nums):
    if len(nums)==1:
        return nums[0]
    first = nums[0]
    mid = nums[len(nums)//2]
    if mid>first:
        if nums[len(nums)//2]>nums[len(nums)//2-1]:
            return sort_double(nums[len(nums)//2:])
    return sort_double(nums[:len(nums)//2])

print(sort_double([1,2,4,5,3,1]))
