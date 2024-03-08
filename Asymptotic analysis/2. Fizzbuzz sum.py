# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23
# Find the sum of alll the multiples of 3 or 5 below 1000

# S = (3 + 6 + 9 + ... + 999) + (5 + 10 + 15 + ... + 995) - (15 + 30 + 45 + ... + 990)
# S = [3 * (333 * 334 / 2)] + [5 * (199 * 200 / 2)] - [15 * (33 * 67)] 