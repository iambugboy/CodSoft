def main():
    task = []

    while True:
        print("\nwelcome to your daily todo list tasks\n")
        print("1.add a task  2.show lsits of tasks  3.mark completed tasks  4.exit\n")
        choice = input("Enter the choices to be entered:  ")

        if choice == '1':
              print()
              n_task = int(input("how many task you want to add to the list\n"))
              for i in range(n_task):
                  tasks=input("enter the task to be enteered: ")
                  task.append({"tasks" : tasks, "done" : False})
                  print("The task is added to the ist")
        elif choice == '2':
            print("Listed tasks are: ")
            for index, tasks in enumerate(task):
                status = "Done" if tasks["done"] else "Not Done"
                print(f"{index + 1}. {tasks['tasks']} - {status}")
        elif choice == '3':
            tasks_index = int(input("Enter the taskk numb to be checked as Done: ")) -1
            if 0<=tasks_index < len(task):
                task[tasks_index]["done"]=True
                print("tasks markde as done")
            else:
                print("please enter valid task number")
        elif choice == '4':
            print("exit the todo list")
            break
        else:
            print("invalid input, please input again")


if __name__ == "__main__":
    main()
