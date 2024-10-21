# Exercise 6: Substring Search

numbers = []
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

sum_of_numbers = sum(numbers)
print(f"\nThe list of numbers: {numbers}")
print(f"The sum of all numbers in the list: {sum_of_numbers}")


largest_number = max(numbers)
smallest_number = min(numbers)
print(f"The largest number in the list: {largest_number}")
print(f"The smallest number in the list: {smallest_number}")