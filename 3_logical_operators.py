# Exercise 3: Logical Operators


bool1 = bool(input("Enter first boolean value : "))
bool2 = bool(input("Enter second boolean value : "))
bool3 = bool(input("Enter third boolean value : "))

and_result = bool1 and bool2 and bool3
or_result = bool1 or bool2 or bool3
not_result = not (bool1 and bool2 and bool3)

print("AND result:", and_result)
print("OR result:", or_result)
print("NOT result:", not_result)