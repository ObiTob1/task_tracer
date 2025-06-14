import json
from datetime import date


def save_changes():
    global tasks

    with open("task_tracker.json", "w+", encoding='utf-8') as file_update:
        json.dump(tasks, file_update, indent=4,ensure_ascii=False)

    print("JSON file was changed successful.\n\n")

def add_task(discr):
    global count_id,tasks,datetime_now

    count_id += 1
    n = count_id

    task = {
        "id": n,
        "description": discr,
        "status": "todo",
        "createdAt": datetime_now,
        "updatedAt": datetime_now
    }
    tasks["tasksList"].append(task)
    print(f"Task added successfully (ID: {count_id}).")
    save_changes()

def update_task(id_task,discr):
    global count_id, tasks,datetime_now

    f = 1
    id_task = int(id_task)
    for task in tasks["tasksList"]:
        if task["id"] == id_task:
            task["description"] = discr
            task['updatedAt'] = datetime_now
            f = 0

    if f == 1:
        print("This ID wasn't found :/")
    else:
        print("The task was updated.")

    save_changes()


def delete_task(id_task):
    global tasks
    indx = 0
    f = 0
    i = 0
    for task in tasks['tasksList']:
        if task['id'] == int(id_task):
            indx = i
            f = 1
            break
        i += 1

    if f == 1:
        tasks["tasksList"].pop(indx)
        print("The task was deleted successfully")
        save_changes()
    else:
        print("The task wasn't found!\n\n")

def mark_in_progress(id_task,first_word):
    global tasks,datetime_now
    f = 0
    for task in tasks['tasksList']:
        if task['id'] == int(id_task):
            task['status'] = first_word[5:]
            task['updatedAt'] = datetime_now
            f = 1

            break

    if f == 0:
        print("The task wasn't found!")
        save_changes()
    else:
        print(f"The status of the task with {id_task} ID has been changed on '{first_word[5:]}' !\n\n")


def list_tasks():
    global tasks
    for task in tasks["tasksList"]:
        print(f"ID-{task['id']} {task['description']} {task['status']}.")
    print('\n\n')

def list_process(second_word):
    for task in tasks["tasksList"]:
        if task['status'] == second_word:
            print(f"ID-{task['id']} {task['description']} {task['status']}.")

    print("\n\n")



count_id = 0
today = date.today()
datetime_now = "{}.{}.{}".format(today.day, today.month, today.year)
print(
"""                      Hello!
    Task tracker is a project used to track and manage your tasks.

You have the right to enter the following commands:

Add - add "Buy groceries"

Update - update 1 "Buy groceries and cook dinner"

Delete - delete 1

Mark a task as in progress or done - mark-in-progress 1
                                     mark-done 1
                                     
List all tasks - list


List all tasks that are done - list done

List all tasks that are not done - list todo

List all tasks that are in progress - list in-progress



""")
while True:
    with open('task_tracker.json',"r",encoding='utf-8') as file_open:
        tasks = json.load(file_open)



        command = input("Please, enter command: \n").split()
        first_word = command[0]

        if first_word == "add":
            discr = ' '.join(command[1:])
            add_task(discr)

        elif first_word == "update":
            id_task = command[1]
            discr = ''.join(command[2:])
            update_task(id_task, discr)

        elif first_word == "delete":
            id_task = command[1]
            delete_task(id_task)

        elif first_word == "mark-in-progress" or first_word == "mark-done":
            id_task = command[1]
            mark_in_progress(id_task,first_word)


        elif first_word == "list":
            try:
                second_word = command[1]
                if second_word in ["todo","in-progress","done"]:
                    list_process(second_word)
                else:
                    print("This word doesn't exist!")
            except IndexError:

                list_tasks()

        else:
            print("This command doesn't exist! \nPlease, try again.\n\n")




