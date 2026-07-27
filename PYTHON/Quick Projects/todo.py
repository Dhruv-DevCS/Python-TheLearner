# Making a Function That prints a list of the all the tasks

def print_tasks(tasks):

    if len(tasks) == 0:
        print("No Pending Tasks!")
        return

    for i in range(len(tasks)):
        print(f"{i}. {tasks[i]}")


# Making a main Function

def main():

    tasks = []      # making an empty task list

    # Runs the loop unless it doesn't quit

    while True:

        # Gives user choice to select the function

        print("\n1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. EXIT")

        try:

            choice = int(input("Enter Your Choice : "))

            # User choses to : 4. Exit

            if choice == 4:
                break

            # User choses to : 1. Add

            elif choice == 1:

                tasks.append(input("Enter Task to add : "))     # Appends task to the list
                print("Task Added Successfully!")

                print_tasks(tasks)                              # Calling Function to print task list

            # User choses to : 2. Edit

            elif choice == 2:

                if len(tasks) == 0:
                    print("You Have no Pending Tasks!")
                    continue

                # Gets indexes of existing task and replace it's task with the new one

                old = int(input("Enter Task Number to replace : "))
                new = input("Enter new Task : ")

                print(f"Task \"{tasks[old]}\" Has been replaced with :")

                tasks[old] = new

                print(f"{new}")

                print_tasks(tasks)                              # Calling Function to print task list

            # User choses to : 3. Remove

            elif choice == 3:

                if len(tasks) == 0:
                    print("You Have no Pending Tasks!")
                    continue

                # using variable to store task to remove

                remove = int(input("Enter Task Number to remove : "))

                # and popping it out

                removed_task = tasks.pop(remove)

                print(f"Task : \"{removed_task}\" has been successfully removed")

                print_tasks(tasks)                              # Calling Function to print task list

            else:
                print("Please Enter a Valid Choice!")

        # Error Handling

        except (ValueError, IndexError):
            print("Please Enter a Valid Number!")


# End Of the program!

if __name__ == "__main__":
    main()