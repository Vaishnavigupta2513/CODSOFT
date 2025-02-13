tasks = []
def add_task(title,description,deadline):
    task = {
        'title':title,
        'description':description,
        'deadline':deadline,
        'status':'pending'
    }
    tasks.append(task)
    print(f"Tash{task} Added Successfully.")
    
def view_task():
    if not tasks:
        print("No Tasks Available")
        return
    for index,tak in enumerate(tasks):
        print(f"{index+1}.{task['title']}-{task['status']}")
        print(f"Description:{task['description']}")
        print(f"Deadlinee:{task['deadline']}")
        print()
def update_task(task_index, status=None, title=None, description=None, deadline=None):
    if task_index < 0 or task_inddex >= len(tasks):
        print("Invalid task index.")
        return
    task = tasks[task_index]
    if status:
        task['status'] = status
    if title:
        task['title'] = title
    if description:
        task['description'] = description
    if deadline:
        task['deadline'] = deadline
    print(f"Task '{task['title']}' updated.")
def delete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index.")
        return
    task = tasks.pop(task_index)
    print(f"Task '{task['title']}' deleted.")
    
while True:
    print("To Do List:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice=input("Enter your choice(1-5):")
    if choice == '1':
        title = input("Enter task title:")
        description = input("Enter task description:")
        deadline = input("Enter task deadline:")
        add_task(title,description,deadline)
    elif choice == '2':
        view_tasks() 
    elif choice == '3':
        view_tasks()
        task_index=int(input("Enter the task number to update:")) 
        new_status=input("Enter new status(Pending/Completed):")
        update_task(task_inndex,status-new_status)
    elif choice == '4':
        view_tasks()
        task_index=int(input("Enter the task number to delete:"))-1
        delete_task(task_index) 
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice,please select valid option")
    
        
