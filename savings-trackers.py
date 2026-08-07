# ---------------------------------------
# Student Savings Tracker
# Developed for VESA Project 1
# ---------------------------------------

# Function to display motivational messages based on savings progress
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


# Display application title
print("=" * 45)
print("      STUDENT SAVINGS TRACKER")
print("=" * 45)

# Ask the user if they want to set a custom savings goal
choice = input("Set your own goal? (yes/no): ").lower()

# Set and validate the savings goal
if choice == "yes":
    goal = float(input("Enter goal amount: ₹"))

    while goal <= 0:
        print("Goal amount must be greater than ₹0.")
        goal = float(input("Enter goal amount: ₹"))
else:
    goal = 500

# Initialize variables
total_savings = 0
week = 1
history = []

print(f"\nYour Savings Goal is: ₹{goal}")

# Continue accepting weekly savings until the goal is reached
while total_savings < goal:

    print(f"\nWeek {week}")

    # Accept weekly savings
    amount = float(input("Enter savings: ₹"))

    # Validate weekly savings
    if amount < 0:
        print("Savings cannot be negative.")
        continue

    # Update total savings and store history
    total_savings += amount
    history.append(amount)

    # Calculate remaining amount
    remaining = goal - total_savings

    # Display current savings
    print(f"Current Savings: ₹{total_savings}")

    # Show remaining amount if goal is not yet reached
    if total_savings < goal:
        print(f"Remaining: ₹{remaining}")

    # Display motivational message
    percent = (total_savings / goal) * 100
    motivation(percent)

    # Move to the next week
    week += 1


# Display final summary
print()
print("=" * 45)
print("🎮 Congratulations!")
print("You have saved enough money to buy your video game!")
print("=" * 45)

print(f"Goal Amount      : ₹{goal}")
print(f"Total Saved      : ₹{total_savings}")
print(f"Extra Savings    : ₹{total_savings - goal}")
print(f"Weeks Required   : {week - 1}")

# Display weekly savings history
print("\nWeekly Savings History")

for i in range(len(history)):
    print(f"Week {i + 1}: ₹{history[i]}")

print("\nThank you for using Student Savings Tracker!")