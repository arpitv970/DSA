# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# Solution:

# 1. State the problem clearly. Identify the input & output formats.
'''
> We can represent sequence of cards as the list of numbers.
> And so, fliping the card equivalent to accessing the value of the number at the corresponding position of that list.

# Problem:
WAP to determine the position of the given number in the list of numbers arranged in decreasing order. Also, minimize the number of times we access the elements from the list.

# INPUT:
> 'cards': list of number sorted in decreasing order
> 'query': A number, whose position is to be determined in the list

# OUTPUT:
> 'position': it is the position of the query inside the list of 'cards'
'''

# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
'''
# Here is the list of possible variations:
> The number 'query' lies somewhere in the middle of the list 'cards'.
> The number 'query' is the first element in 'cards'.
> The number 'query' is the last element in 'cards'.
> The list 'cards' have only single element, i.e. 'query'.
> The list 'cards' is empty.
> The list 'cards' don't contain 'query'.
> The list 'cards' contains repeating elements.
> The list 'cards' have repeating 'query'.
'''
tests = []

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

# query is the first element
tests.append({
        'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# We will assume that our function will return '-1' in case 'cards' does not contain 'query'.
# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# In the case where 'query' occurs multiple times in 'cards', we'll expect our function to return the first occurrence of 'query'.
# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# print(tests)

# 3. Come up with a correct solution for the problem. State it in plain English.
'''
In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:

> Create a variable 'position' with the value 0.
> Check whether the number at index 'position' in 'card' equals 'query'.
> If it does, 'position' is the answer and can be returned from the function
> If not, increment the value of 'position' by 1, and repeat steps 2 to 5 till we reach the last 'position'.
> If the number was not found, return '-1'.
'''
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
'''def locate_card(cards, query):
    # Create a variable 'position' with the value 0.
    position = 0
        
    # Setting loop for repetition
    while position < len(cards):

        # Check if element at the current position matches the 'query'
        if cards[position] == query:
            return position
        # Increment in position
        position += 1
    return -1

cards5 = tests[5]['input']['cards']
query5 = tests[5]['input']['query']

locate_card(cards5, query5)'''

# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
'''
> Recall this statement from original question: "Alice challenges Bob to pick out the card containing a given number by turning over as few cards as possible." We restated this requirement as: "Minimize the number of times we access elements from the list cards"

> Befor we minimize the number, we need to measure it.
> Since, we access a list element once in every iteration, for a list of size 'N' we access elements from list up to 'N' times.
> Thus, we need to overturn up to 'N' cards in the worst case, to find out the required card.
'''

# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
'''
> At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. This is called a brute force approach.
> The best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. 
> In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called 'binary search'.
'''

# 7. Come up with a correct solution for the problem. State it in plain English.
'''
Here's how binary search can be applied to our problem:
> Find the middle element of the list.
> If it middle element == query, return middle element as answer
> If it middle element < query, then repeat the search in the first half of the list (REMINDER: in this particular question the list is sorted in descending order.)
> If it middle element > query, then repeat the search in the second half of the list
> If no more elements remains, return -1.
'''

# 8. Implement the solution and test it using example inputs. Fix bugs, if any.
'''
Here's an implementation of binary search for solving our problem. We also print the relevant variables in each iteration of the while loop.
'''
'''def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi)//2
        mid_number = cards[mid]

        print("lo: ", lo, "hi:" , hi, "mid: ", mid, "mid_number: ", mid_number)
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1'''
'''
> There is an issue in above code, when it comes to situations like in the last test case
> When we find that 'cards[mid]' is equal to 'query', we need to check whether it is the first occurrence of 'query' in the list i.e the number that comes before it.
> we'll define a helper function called 'test_location', which will take the list 'cards', the 'query' and 'mid' as inputs.
'''
'''def test_location(cards, query, mid):
    mid_number = cards[mid]
    
    print("mid: ", mid, "mid_number: ", mid_number)

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo: ", lo, "hi: ", hi)
        mid = (lo + hi)//2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1'''

# Here is the final code for the algorithm (without the print statements):
def test_location(cards, query, mid):
    mid_number = cards[mid]
    
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi)//2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# 9. Analyze the algorithm's complexity and identify inefficiencies, if any.
'''
Once again, let's try to count the number of iterations in the algorithm. If we start out with an array of 'N' elements, then each time the size of the array reduces to half for the next iteration, until we are left with just 1 element.

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