# You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
# Give an algorithm that identifies the second-largest number in the array, and
# that uses at most n + logn - 2 comparisons.

def second_largest(nums):
    if len(nums)==2:
        if nums[0]>nums[1]:
            return nums[0],nums[1]
        return nums[1],nums[0]
    lmax,lsmax = second_largest(nums[:len(nums)//2])
    rmax,rsmax = second_largest(nums[len(nums)//2:])
    max_element = None
    second_max_element = None
    if lmax>rmax:
        max_element = lmax
        if rmax>lsmax:
            second_max_element = rmax
        else:
            second_max_element = lsmax
    else:
        max_element = rmax
        if lmax>rsmax:
            second_max_element = lmax
        else:
            second_max_element = rsmax
    return max_element,second_max_element
print(second_largest([1,2,3,4,5,6,7,8]))
