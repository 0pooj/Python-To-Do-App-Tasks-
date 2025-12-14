import json
import os

FILE_NAME = "tasks.json"

tasks = [] 

def load_tasks():
    """Load tasks from the JSON file on startup."""
    global tasks
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
            print(f"✅ Loaded {len(tasks)} tasks from {FILE_NAME}.")
        except json.JSONDecodeError:
            print("⚠️ JSON file is empty or invalid. Starting with an empty task list.")
            tasks = []
        except Exception as e:
            print(f"❌ An error occurred during loading: {e}")
            tasks = []
    else:
        print("ℹ️ Task file not found, starting with an empty list.")

def save_tasks():
    """Save tasks to the JSON file."""
    try:
        
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
         
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        
    except Exception as e:
        print(f"❌ An error occurred during saving: {e}")



def show_menu():
    print("\n--- To-Do App ---")
    print(" 1. Add task")
    print(" 2. View tasks")
    print(" 3. Delete task")
    print(" 4. Exit")

def add_task():
    global tasks 
    task = input("Enter the task name: ")
    tasks.append(task)
    save_tasks() 
    print("✅ The task has been added")

def show_tasks():
    if not tasks:
        print("❌ No tasks")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            
def delete_task():
    global tasks 
    show_tasks()
    
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 0 < task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks() 
                print(f"🗑️ The task has been deleted: {deleted_task}")
            else:
                print("❌ The number entered is outside the scope of the tasks presented.")
        except ValueError:
            print("❌ The entry is incorrect. Please enter a number.")
        

load_tasks()

while True:
    show_menu()
    choice = input("Choose a number: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        
        save_tasks() 
        print("👋 Good bye")
        break
    else:
        print("❌ Incorrect choice")
