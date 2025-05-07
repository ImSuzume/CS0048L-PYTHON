"""
Create a simple to-do list application that allows users to add,
remove, and view tasks. The program should display a menu with
options for each action. The program should continue to run until
the user chooses to exit.
"""
myTasks={}

def menu ():
    print("==============================")
    print ("1. Add Task")
    print ("2. Remove Task")
    print ("3. View Task")
    print ("4. Exit")
    print("==============================")
    
def addTask():
    global myTasks
    task_name = input("Add a new task: ").lower()
    task_desc = input("Add description: ").lower()
    myTasks[task_name]=task_desc
    
def RemoveTask(): 
    global myTasks
    ViewTask()
    remove = input("Select task to remove: ").lower()
    if remove in myTasks:
        del myTasks[f"{remove}"]
        print("Successfully removed task.")
    else:
        print("Invalid input.")
    
def ViewTask():
    if (myTasks=={}):
        print ("")
        print ("No Tasks added.")
    else:
        for  task_name, task_desc in myTasks.items():
            print(f"{task_name}: {task_desc}")
        
def main():
    global myTasks
    choice=0
    while (choice!="4"):
        menu()
        choice = input("Select an option: ").lower()
        if choice=="1":
            addTask()
        elif choice=="2":
            RemoveTask()
        elif choice=="3": 
            ViewTask()   
        elif choice == "4":
            print("See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")
main()