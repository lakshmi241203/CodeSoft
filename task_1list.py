import pickle

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

def save_tasks(tasks, filename='tasks.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(tasks, file)

def load_tasks(filename='tasks.pkl'):
    try:
        with open(filename, 'rb') as file:
            tasks = pickle.load(file)
            return tasks
    except FileNotFoundError:
        return []

def add_task(tasks, description):
    task = Task(description)
    tasks.append(task)
    save_tasks(tasks)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].mark_completed()
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
