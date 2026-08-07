print("===================================")
print("     STUDENT SAVINGS TRACKER")
print("===================================")

choice = input("Set your own goal? (yes/no): ").lower()

if choice == "yes":
    goal = float(input("Enter goal amount: ₹"))
else:
    goal = 500

total_savings = 0
week = 1

print("Savings Goal: ₹", goal)

while total_savings < goal:

    print("\nWeek", week)

    amount = float(input("Enter savings: ₹"))

    if amount < 0:
        print("Savings cannot be negative.")
        continue

    total_savings += amount

    remaining = goal - total_savings

    print("Current Savings: ₹", total_savings)

    if total_savings < goal:
        print("Remaining: ₹", remaining)

    week += 1

print("\nGoal Achieved!")