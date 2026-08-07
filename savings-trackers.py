def motivation(percent):
    if percent < 25:
        print("🌱 Great start!")
    elif percent < 50:
        print("💪 Keep going!")
    elif percent < 75:
        print("🚀 More than halfway!")
    elif percent < 100:
        print("🔥 Almost there!")
    else:
        print("🎉 Goal achieved!")


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

    percent = (total_savings / goal) * 100
    motivation(percent)

    week += 1

print("\nGoal Achieved!")