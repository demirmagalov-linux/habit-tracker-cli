import json
import os
from datetime import date, timedelta

FILE_PATH = "habits.json"


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return {}
    
def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)


def log_habits(data, habits):
    today = str(date.today())
    data[today] = habits    
    return data

def get_streak(data, habit):
    streak = 0
    day = date.today()

    while True:
        day_str = str(day)

        if day_str in data and habit in data[day_str]:
            streak += 1
            day = day - timedelta(days=1)  
        else:
            break  

    return streak  

def main():
    data = load_data(FILE_PATH)

    while True:
        command = input("Enter command (log, stats, quit): ").strip().lower()

        if command == "quit":
            break

        elif command == "log":
            done_habits = input("What Habits have you done today? \nInput: ").strip().lower().split()
            data = log_habits(data, done_habits)
            save_data(FILE_PATH, data)

        elif command == "stats":
            unique_habits = set()
            for habit_list in data.values():
                for habit in habit_list:
                    unique_habits.add(habit)

            for habit in unique_habits:
                streak = get_streak(data, habit)
                print(f"{habit}, streak: {streak}")
main()
