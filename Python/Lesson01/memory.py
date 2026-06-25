x = 10
y = x

print("Before changing x")
print("x =", x, "id=", id(x))
print("y =", y, "id=", id(y))

x = 20

print("\nAfter changing x")
print("x =", x, "id=", id(x))
print("y =", y, "id=", id(y))
