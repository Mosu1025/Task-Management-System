 # Task Management Application

With the following capabilities, this Python terminal programme offers a basic task management system:

 - Add new tasks with the following information: name, description, category, priority, and deadline.
 - View every task along with its due date, category, priority, and status.
 - Declare a task as finished.
 - From the list of available tasks, remove a task.
 - Any task can be prioritised by setting its priority.
 - Search for tasks whose names include a particular term.
 - Assign each work to a certain category to classify it.
 - Give an assignment a due date.

## How to Run the Application
### Prerequisites
Make sure your computer is running Python. If not, go to python.org to download and install Python.
### Steps

**1.  Clone the Repository:**

```bash
git clone https://github.com/mohsanNasir/task-management.git
cd task-management
```
**2. Run the Python script.**
```bash
python task_manager.py
```
**3. Use the Task Management**

A menu with several options will be displayed by the application. To execute an action, enter the correct number.

**Add New Task (Option 1):**
Input the necessary information for the new task, including its name, description, category, priority, and due date.<br/>
**View All Tasks (Option 2):**
shows a list of every task along with its specifics.
**Mark Task as Completed (Option 3):**
Type the task name to indicate that it has been finished.
**Delete Task From Available Tasks List (Option 4):**
Type in the task's name to be deleted.
**Prioritize Any Task (Option 5):**
Put the task name and the new priority (High, Medium, Low) in here.
**Search Tasks From Available Tasks (Option 6):**
To find a keyword in task names, enter it here.
**Categorize Any Task (Option 7):**
Put the task name and the new category in here.
**Set Due Date for a Task (Option 8):**
In the format YYYY-MM-DD, provide the task name and the new due date.
**Quit Task Manager (Option 9):**
Closes the application.

**4. Explore Task Management:**
To properly manage your work and navigate through the available options, adhere to the on-screen directions.


## Example Usage
1.  Add a new task:
```Enter New task name: Assignment 
 Enter task description: College Software development assessment  
 Enter task priority (High-Medium-Low): High 
 Enter task category: College work
 Enter due date (YYYY-MM-DD): 2024-01-31```
```
2. View all tasks: 
``` Enter the task name to mark as completed: Assignment 
Task "Assignment" marked as completed.```
```

3.  Mark a task as Completed

```Tasks:  1. Task Name: Assignment - Status:  Pending  |  Priority: High  | Category:  Collage work  1  |  Due Date:  2024-01-31```

