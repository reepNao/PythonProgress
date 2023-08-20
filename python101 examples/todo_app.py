# -*- coding: utf-8 -*-

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task Added:", task)

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print("%d %s " % (idx, task))
        else:
            print("There is no task to be done.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print("Completed task:", completed_task)
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. The job is done")
        print("4. Exit\n")
        choice = input("\nMake your selection: ")

        if choice == "1":
            task = input("\nEnter the new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            todo_list.show_tasks()
            task_index = int(input("\nEnter the number of the completed task: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            print("Exiting...\n")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
