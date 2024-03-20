# Prompt user for the starting value
start_value = int(input("Enter start value: "))

# Prompt user for the stopping value
stop_value = int(input("Enter stop value: "))

# Prompt user for the increment value
increment_value = int(input("Enter increment value: "))

# Loop from start_value to stop_value, incrementing by increment_value
while start_value <= stop_value:
    print(start_value)
    start_value += increment_value


