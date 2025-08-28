a = 5
b = 6

# Using conditionals with comparison operators
if a > b:
    print(f"{a} > {b}: True")
else:
    print(f"{a} > {b}: False")

if a < b:
    print(f"{a} < {b}: True")
else:
    print(f"{a} < {b}: False")

if a >= b:
    print(f"{a} >= {b}: True")
else:
    print(f"{a} >= {b}: False")

if a <= b:
    print(f"{a} <= {b}: True")
else:
    print(f"{a} <= {b}: False")

if a == b:
    print(f"{a} == {b}: True")
else:
    print(f"{a} == {b}: False")

if a != b:
    print(f"{a} != {b}: True")
else:
    print(f"{a} != {b}: False")

# Specific example with conditional
print(f"\nSpecific example with conditional:")
if 5 > 6:
    print(f"5 > 6: True")
else:
    print(f"5 > 6: False")
    

monthly_entry = 5000

if(monthly_entry>=5000):
    print("You can apply for the credit card")
elif(monthly_entry>=10000):
    print("You can apply for the premium credit card")
else:
    print("You cannot apply for the credit card")
    
