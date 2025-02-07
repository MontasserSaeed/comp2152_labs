"""
Author: <YOUR REAL FIRST AND LAST NAME>
Assignment: #1
"""

# Define variables with appropriate comments
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5  # Float
highest_reps = 25  # Integer
membership_active = True  # Boolean

# Define a dictionary to store workout statistics
# Dictionary: Keys are friend names (strings), values are tuples containing workout minutes (integers)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 25),
    "Taylor": (50, 60, 30)
}

# Calculate total workout minutes for each friend and store in dictionary
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

# Create a 2D list (nested list) for workout minutes
# List of lists: Each inner list represents a friend, and each column represents an activity
workout_list = [list(minutes) for friend, minutes in workout_stats.items() if "_Total" not in friend]

# Slicing workout_list
# Extract and print yoga and running minutes for all friends
print("Yoga and Running Minutes:")
for row in workout_list:
    print(row[:2])

# Extract and print weightlifting minutes for the last two friends
print("Weightlifting Minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2])

# Check if any friend's total workout minutes are >= 120 and print a message
for friend, total_minutes in workout_stats.items():
    if "_Total" in friend and total_minutes >= 120:
        print(f"Great job staying active, {friend.split('_')[0]}!")

# Allow user input to check friend's workout details
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    minutes = workout_stats[friend_name]
    total_minutes = workout_stats.get(f"{friend_name}_Total", 0)
    print(f"{friend_name}'s workout minutes: Yoga: {minutes[0]}, Running: {minutes[1]}, Weightlifting: {minutes[2]}")
    print(f"Total Workout Minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Determine the friend with the highest and lowest total workout minutes
friend_totals = {friend: total for friend, total in workout_stats.items() if "_Total" in friend}
max_friend = max(friend_totals, key=friend_totals.get).replace("_Total", "")
min_friend = min(friend_totals, key=friend_totals.get).replace("_Total", "")

print(f"Friend with highest workout minutes: {max_friend}")
print(f"Friend with lowest workout minutes: {min_friend}")
