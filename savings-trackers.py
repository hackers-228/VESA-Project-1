print("===================================")
print("     STUDENT SAVINGS TRACKER")
print("===================================")

goal = 500
total_savings = 0
week = 1

while total_savings < goal:
    print("\nWeek", week)

    amount = float(input("Enter savings: ₹"))

    total_savings += amount

    print("Current Savings: ₹", total_savings)

    week += 1

print("\nGoal Achieved!")