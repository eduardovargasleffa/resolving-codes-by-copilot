# let's calculate the average of three scores provided in the user input. A tip is: use arithmethic operators to perform the average calculation.

data = input("Enter three scores separated by spaces: ")

# Split the input string into a list of strings
scores = data.split()
# Convert the list of strings to a list of floats
scores = [float(score) for score in scores]
# Calculate the average
average = sum(scores) / len(scores)
# Print the average
print(f"The average of the three scores is: {average:.2f}")
