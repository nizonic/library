a = 1
b = 2
c = 3
d = 4

# Change the function below to calculate the result
# with the given formula:
# `a - (b^2 / (c - d * (a + b)))`
# You must use the variables defined above.
def calculate():
    res = 0.0
    res = a - ((b**2) / (c - d * (a + b)))

    # You don't need to change the following line.
    # It simply returns the value calculated above.
    return res
print(calculate())
