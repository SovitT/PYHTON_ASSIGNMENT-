# Exercise 9: Sorting a List

numbers = []
for i in range(5):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

ascending_order = sorted(numbers)
print(f"\nList in ascending order: {ascending_order}")

descending_order = sorted(numbers, reverse=True)
print(f"List in descending order: {descending_order}")