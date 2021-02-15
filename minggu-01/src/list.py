squares = [1, 4, 9, 16, 25]
squares

squares[0]  # indexing returns the item
squares[-1]
squares[-3:]  # slicing returns a new list
squares[3] = 64  # replace the wrong value
squares

squares.append(216)  # add the cube of 6
squares.append(7 ** 3)  # and the cube of 7
squares

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters

# now remove them
letters[2:5] = []
letters

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]