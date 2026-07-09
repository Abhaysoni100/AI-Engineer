print("=" * 40)
print("     Welcome to Python ATM")
print("=" * 40)

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice=int(input("Enter your choice:"))

if choice==1:
    print("Your balance is ₹25000")
elif choice==2:
    print("Deposit feature is comning tomorrow")
elif choice==3:
    print("Withdraw feature is coming tomorrow")
elif choice==4:
    print("Thank you for using our ATM")
else:
    print("Invalid choice. Please try again.")

