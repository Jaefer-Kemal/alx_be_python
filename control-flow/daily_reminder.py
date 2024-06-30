task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        result = f"'{task}' is a high priority task"
    case "medium":
        result = f"'{task}' is a medium priority task"
    case "low":
        result = f"'{task}' is a low priority task"

if time_bound == "yes":
    print(f"Reminder: {result} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note : {result}. Consider completing it when you have free time.")
          
