marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Fail")

print("\n Result generated succesfully.....")

# A common interview question is:
# Why should higher conditions come before lower conditions?
# A good answer is: "Python executes only the first matching condition in an if-elif-else chain.
# If a broader condition like marks >= 40 comes first, it prevents more specific conditions like marks >= 90 from ever
# being checked."