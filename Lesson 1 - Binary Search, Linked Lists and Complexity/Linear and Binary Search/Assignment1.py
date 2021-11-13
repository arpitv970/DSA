# Assignment 1 - Binary Search Practice
# Problem - Rotated Lists
'''
We'll solve the following problem step-by-step:

> You are given list of numsbers, obtained by rotating a sorted list an unknown numsber of times. Write a function to determine the minimum numsber of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numsbers in the list are unique.
> Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
> According to question "rotating a list" is defined as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 
>"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
'''
# Solution:

# 1. State the problem clearly. Identify the input & output formats.
'''
# Problem:
> WAP to determine the position of the 'min_nums' from 'nums', as its position will be the numsber of times list rotated.
> If 'min_nums' is not found in the list, then no rotation would be considered

# INPUT:
> 'nums': rotated list which was sorted before rotation

# OUTPUT:
> 'rotations': numsber of times sorted list was rotated

'''
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
'''
# Here is the list of possible variation:
> if 'min_nums' lies somewhere in middle of the list 'nums'.
> if 'min_nums' is the first element of the list 'nums'.
> if 'min_nums' is the last element of the list 'nums'.
> if list 'nums' have only single element
> if list 'nums' is empty
'''
tests = []

# if 'min_nums' lies somewhere in middle of the list 'nums'.
tests.append({
    'input': {
        'nums': [4, 5, 1, 2, 3]
    },
    'output': 2
})

# if 'min_nums' is the first element of the list 'nums'.
tests.append({
    'input': {
        'nums': [1, 2, 3, 4, 5]
    },
    'output': 0
})

# if 'min_nums' is the last element of the list 'nums'.
tests.append({
    'input': {
        'nums': [2, 3, 4, 5, 1]
    },
    'output': 4
})

# if list 'nums' have only single element
tests.append({
    'input': {
        'nums': [3]
    },
    'output': 0
})

# if list 'nums' is empty
tests.append({
    'input': {
        'nums': []
    },
    'output': 0
})

# 3. Come up with a correct solution for the problem. State it in plain English.
'''
To solve this: we should find the position of the smallest numsber as numsber of times rotation happens, the same numsber of times smallest numsber will increases its index with 1. So the problem is now converted to find the position of smallest numsber in 'nums'. Here's how we implement it:
> Create a variable 'min_nums' with any value, say 0.
> Now compare current position element of 'nums' with 'min_nums'.
> If current position element < 'min_nums', then set 'min_nums' value to current position element of 'nums'
> If above is not true, then do not change value of 'min_nums'.
> Proceed with step 3 to 6 till we reach the last element.
> If 'min_nums' is not found then no rotation would be considerd.
'''
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.

'''def count_rotations(nums):
    # Create a variable 'min_nums' with any value, say 0.
    min_nums = max(nums)
    # print('min_nums: ', min_nums, '\nnums: ', nums)
    for i in range(len(nums)):
        # Now compare current position element of 'nums' with 'min_nums'.
        # print(f'\nindex:{i} = {nums[i]}', end=' ',)
        if nums[i] < min_nums:
            min_nums = nums[i]
    return print(min_nums)

print('Test Case[0]: ', tests[0])
nums1 = tests[0]['input']['nums']
count_rotations(nums1)
'''
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
'''
> Since, we access a list element once in every iteration, from list of size 'N' we access elements from the list up to 'N' times.
> In the worst case we need to access 'N' elements of the list
'''

# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
'''
> At the moment, we're simply comparing every element of the list one by one, without utilizing the fact that given list is the rotation of a sorted list.
> As we know in the 'nums', if we compare any two adjacent elements and if right one is found to be smaller than left, it would be the smallest in the list
> So we can use above fact, and can apply this using binary search algo.
'''

# 7. Come up with a correct solution for the problem. State it in plain English.
'''
Here's how binary search can be applied to our problem:
> Find the middle element, say mid, of the list
> Now compare mid, mid - 1, mid + 1
> If minimum numsber is neither mid nor mid + 1, the it must lie either left or right side of the list.
> If middle element is greater than last numsber, then minimum numsber lies on the right side.
> If middle element is smaller than last numsber, then minimum numsber lies on the left side.
'''

# 8. Implement the solution and test it using example inputs. Fix bugs, if any.
'''
Here's an implementation of binary search for solving our problem. We also print relevent variables.
'''

def count_rotations(nums):
    lo, hi = 0, len(nums)-1
    print('lo:', lo, ', hi:', hi)

    # if no elements in the list
    if len(nums)==0:
        hi += 1

    for i in range(lo, hi+1):
        print('lo:', lo, ', hi:', hi)

        # if list is rotated at all
        if hi < lo:
            return print(0)

        # if there is only one element left
        if lo == hi:
            return print(lo)

        # finding the mid element
        mid = (lo + hi)//2
        print('mid:', mid)

        # Check if element mid+1 is minimum element
        if mid < hi and nums[mid + 1] < nums[mid]:
            return print('OUTPUT:', mid+1)
        
        # Check if mid element is minimum
        if mid > lo and nums[mid] < nums[mid - 1]:
            return print('OUTPUT:', mid)
        
        # Direction test for search
        if nums[mid] > nums[hi]:
            lo = mid + 1
        
        else:
            hi = mid - 1

# Testing Test Cases
nums1 = tests[0]['input']['nums']
print('Test Case[0]: ', tests[0])
count_rotations(nums1)

nums2 = tests[1]['input']['nums']
print('Test Case[1]: ', tests[1])
count_rotations(nums2)

nums3 = tests[2]['input']['nums']
print('Test Case[2]: ', tests[2])
count_rotations(nums3)

nums4 = tests[3]['input']['nums']
print('Test Case[3]: ', tests[3])
count_rotations(nums4)

nums5 = tests[4]['input']['nums']
print('Test Case[4]: ', tests[4])
count_rotations(nums5)


# Here is the final code for the algorithm (without the print statements):
def count_rotations(nums):
    lo, hi = 0, len(nums)-1

    # if no elements in the list
    if len(nums)==0:
        hi += 1

    for i in range(lo, hi+1):

        # if list is rotated at all
        if hi < lo:
            return 0

        # if there is only one element left
        if lo == hi:
            return lo

        # finding the mid element
        mid = (lo + hi)//2
        
        # Check if element mid+1 is minimum element
        if mid < hi and nums[mid + 1] < nums[mid]:
            return mid + 1
        
        # Check if mid element is minimum
        if mid > lo and nums[mid] < nums[mid - 1]:
            return mid
        
        # Direction test for search
        if nums[mid] > nums[hi]:
            lo = mid + 1
        
        else:
            hi = mid - 1

# 9. Analyze the algorithm's complexity and identify inefficiencies, if any.
'''
> Once again, let's try to count the number of iterations in the algorithm.
> If we start out with an array of 'N' elements, then each time the size of the array reduces to half for the next iteration, until we are left with just 1 element.

Initial length - 'N'

Iteration 1 - 'N/2'

Iteration 2 - 'N/4' i.e. 'N/2^2'

Iteration 3 - 'N/8' i.e. 'N/2^3'

...

Iteration k - 'N/2^k'

Since the final length of the array is 1, we can find the

'N/2^k = 1'

Rearranging the terms, we get

'N = 2^k'

Taking the logarithm

'k = log N'

Where 'log' refers to log to the base 2. Therefore, our algorithm has the time complexity 'O(log N)'. This fact is often stated as: binary search runs in logarithmic time. You can verify that the space complexity of binary search is 'O(1)'.
'''
nums1 = tests[0]['input']['nums']
print('Test Case[0]: ', tests[0])
print(count_rotations(nums1))