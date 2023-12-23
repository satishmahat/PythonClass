#Project 1: To-Do List

tasks=[]


while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. View task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter new task:")
        tasks.append(task)
    
    elif choice == '2':
        task = input("Enter a task to remove:")

        if task in tasks:
            tasks.remove(task)
        else:
            print("No such task found..")

    elif choice=='3':
        print("Tasks")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}:{task}")

    elif choice=='4':
        break
    else:
        print("Invalid choice. Please try again..")

        
