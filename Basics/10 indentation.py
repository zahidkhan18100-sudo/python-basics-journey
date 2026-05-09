# Basic indentation
# Indentation tells Python which code belongs to which block
if True:
    print("Inside block")

print("Outside block")


# Same indentation level
if True:
    print("Line 1")
    print("Line 2")


# Wrong indentation (will give error)
# if True:
# print("Error")


# Nested indentation
if True:
    print("Level 1")
    
    if True:
        print("Level 2")

# If-Else example
x = 10

if x > 5:
    print("Greater")
else:
    print("Smaller")
