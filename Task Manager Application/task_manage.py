class Task:
    def __init__(self, name, description, priority=None, category=None, due_date=None):
        self.name = name
        self.description = description
        self.completed = False
        self.priority = priority
        self.category = category
        self.due_date = due_date


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, priority=None, category=None, due_date=None):
        task = Task(name, description, priority, category, due_date)
        self.tasks.append(task)
        print(f'Task "{name}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                name = f'Task Name:  {task.name} '
                status = "Done" if task.completed else "Pending"
                priority = f'Priority: {task.priority}' if task.priority else ''
                category = f'Category: {task.category}' if task.category else ''
                due_date = f'Due Date: {task.due_date}' if task.due_date else ''
                print(f'{index}. {name} - Status: {status} | {priority} | {category} | {due_date}')

    def mark_completed_task(self, task_name):
        task = self.find_task_by_name(task_name)
        if task:
            task.completed = True
            print(f'Task "{task.name}" marked as completed.')
        else:
            print(f'Task "{task_name}" not found.')

    def delete_task(self, task_name):
        task = self.find_task_by_name(task_name)
        if task:
            self.tasks.remove(task)
            print(f'Task "{task.name}" deleted.')
        else:
            print(f'Task "{task_name}" not found.')

    def prioritize_task(self, task_name, priority):
        task = self.find_task_by_name(task_name)
        if task:
            task.priority = priority
            print(f'Task "{task.name}" prioritized as {priority}.')
        else:
            print(f'Task "{task_name}" not found.')

    def search_tasks(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task.name.lower()]
        if not matching_tasks:
            print(f'No tasks found containing "{keyword}".')
        else:
            print(f'Tasks containing "{keyword}":')
            for index, task in enumerate(matching_tasks, start=1):
                print(f'{index}. {task.name}')
        return matching_tasks  # Always return the list of matching tasks

    def categorize_task(self, task_name, category):
        task = self.find_task_by_name(task_name)
        if task:
            task.category = category
            print(f'Task "{task.name}" categorized as {category}.')
        else:
            print(f'Task "{task_name}" not found.')

    def set_due_date(self, task_name, due_date):
        task = self.find_task_by_name(task_name)
        if task:
            task.due_date = due_date
            print(f'Due date set for task "{task.name}": {due_date}.')
        else:
            print(f'Task "{task_name}" not found.')

    def find_task_by_name(self, task_name):
        for task in self.tasks:
            if task_name.lower() == task.name.lower():
                return task
        return None


def main():
    task_manager = TaskManager()

    while True:
        print('\nTask Management Main Menu:')
        print('1. Add New Task')
        print('2. View All Tasks')
        print('3. Mark Task as Completed')
        print('4. Delete Task From Available Tasks List')
        print('5. Prioritize Task Any Task')
        print('6. Search Tasks From task available')
        print('7. Categorize any Task')
        print('8. Set Due Date for an Task')
        print('9. Quit Task Manager')

        choice = input('Enter your choice from Task Manager Options: ')

        if choice == '1':
            name = input('Enter New task name: ')
            description = input('Enter task description: ')
            priority = input('Enter task priority (High/Medium/Low): ')
            category = input('Enter task category: ')
            due_date = input('Enter due date (YYYY-MM-DD): ')
            task_manager.add_task(name, description, priority, category, due_date)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            task_name = input('Enter the task name to mark as completed: ')
            task_manager.mark_completed_task(task_name)
        elif choice == '4':
            task_manager.view_tasks()
            task_name = input('Enter the task name to delete: ')
            task_manager.delete_task(task_name)
        elif choice == '5':
            task_manager.view_tasks()
            task_name = input('Enter the task name to prioritize: ')
            priority = input('Enter task priority (High/Medium/Low): ')
            task_manager.prioritize_task(task_name, priority)
        elif choice == '6':
            keyword = input('Enter keyword to search for: ')
            task_manager.search_tasks(keyword)
        elif choice == '7':
            task_manager.view_tasks()
            task_name = input('Enter the task name to categorize: ')
            category = input('Enter task category: ')
            task_manager.categorize_task(task_name, category)
        elif choice == '8':
            task_manager.view_tasks()
            task_name = input('Enter the task name to set due date: ')
            due_date = input('Enter due date (YYYY-MM-DD): ')
            task_manager.set_due_date(task_name, due_date)
        elif choice == '9':
            print('Exiting Task Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')


if __name__ == "__main__":
    main()
