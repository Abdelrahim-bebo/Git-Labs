# Simple Task Tracker
tasks = ["Setup Git", "Create SSH Key", "Write Script"]

print("--- My To-Do List ---")

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

new_task = "Learn Branching"
tasks.append(new_task)
print(f"Added: {new_task}")
#This is the line after deletion
# ------Lab Done------
