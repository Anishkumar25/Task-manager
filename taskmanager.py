class Task:
    def __init__(self,task_name,priority,deadline,completed=False):
        self.completed = completed
        self.task_name = task_name
        self.priority = priority
        self.deadline = deadline
    def mark_done(self):
        self.completed = True
    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{status} - {self.task_name}"
    def edit(self, task_name=None, priority=None, deadline=None):
        if task_name is not None:
            self.task_name = task_name
        if priority is not None:
            self.priority = priority
        if deadline is not None:
            self.deadline = deadline

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self,task_name,priority,deadline):
        task = Task(task_name,priority,deadline)
        self.tasks.append(task)
    def view_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
    def mark_task_done(self,task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_done()
        else:
            print("Invalid task index.")
    def delete_task(self,task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")
    def edit_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            print("\nEdit Task Menu")
            print("1. Edit Task Name")
            print("2. Edit Priority")
            print("3. Edit Deadline")
            print("4. Back")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                new_name = input("Enter new task name: ")
                self.tasks[task_index].edit(task_name=new_name)
            elif choice == '2':
                new_priority = input("Enter new priority: ")
                self.tasks[task_index].edit(priority=new_priority)
            elif choice == '3':
                new_deadline = input("Enter new deadline: ")
                self.tasks[task_index].edit(deadline=new_deadline)
            elif choice == '4':
                return
            else:
                print("Invalid choice.")
        else:
            print("Invalid task index.")

manager=TaskManager()
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            task_name = input("Enter task name: ")
            priority = input("Enter task priority: ")
            deadline = input("Enter task deadline: ")
            manager.add_task(task_name,priority,deadline)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as done: ")) - 1
            manager.mark_task_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: ")) - 1
            manager.delete_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter task index to edit: ")) - 1
            manager.edit_task(task_index)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
        main()