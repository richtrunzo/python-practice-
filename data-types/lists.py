 # Lists are very similar to arrays.

 nums = [0, 1, 2, 3, 4, 5]

 nums[0] # returns 0

 nums[-1] #returns 5

 nums[-3] # returns [3, 4, 5]

 nums + [10, 11, 12]  # returns [0, 1, 2, 3, 4, 5, 10, 11, 12]

 nums.append(10 * 3) # returns [0, 1, 2, 3, 4, 5, 10, 11, 12, 30]

letters = ['a', 'b', 'c', 'd']

letters.append('e') # returns ['a', 'b', 'c', 'd', 'e']

letters(2:5) = ['x', 'y', 'z'] # returns ['a', 'b', 'x', 'y', 'z']

letters(2:5) = [] # returns ['a', 'b']

letters[:] = [] # returns []

test = [5, 6, 7, 8]

len(test)  # returns 4

new_test = ['a', 'b', 'c']

mixed = [test, new_test] # returns [[5, 6, 7, 8], ['a', 'b', 'c']]
