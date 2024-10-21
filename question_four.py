#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

# SOLUTION

favourite_food = ['rice', 'chicken', 'liver', 'pork', 'cassava']

# # add two more

favourite_food.append("chips")
favourite_food.append("pizza")

# remove one item

favourite_food.remove("pork")

print("Updated list of foods: \n")
print(favourite_food)






#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list. 

# SOLUTION

# Priniting first and last number
numbers = [2, 5, 8, 10, 3, 6]
first_number = numbers[0]
last_number = numbers[5]
print(f"The first number is {first_number} and last number is {last_number}")

# list in reverse

list_reverse = numbers.reverse()
print(numbers)


# sum of all numbers

number_summation = sum(numbers)

print (f"The sum of all numbers in the list is {number_summation}")