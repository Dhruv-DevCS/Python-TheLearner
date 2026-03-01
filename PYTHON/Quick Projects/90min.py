from datetime import datetime, timedelta

# Get user input
start_time_str = input("Enter start time (HH:MM, 24-hour format): ")

# Parse the time
start_time = datetime.strptime(start_time_str, "%H:%M")

# 90-minute interval
interval = timedelta(minutes=90)

current_time = start_time
times = []

# Generate times for the next 24 hours
for _ in range(16):  # 16 × 90 minutes = 24 hours
    times.append(current_time.strftime("%H:%M"))
    current_time += interval

# Display results
print("\nTimes every 90 minutes:")
for t in times:
    print(t)

input()