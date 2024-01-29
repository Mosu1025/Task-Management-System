import unittest
from task_manage import Task, TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_mark_completed_task(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.mark_completed_task("Task 1")
        self.assertTrue(self.task_manager.tasks[0].completed)

    def test_delete_task(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.delete_task("Task 1")
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_prioritize_task(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.prioritize_task("Task 1", "Low")
        self.assertEqual(self.task_manager.tasks[0].priority, "Low")

    def test_search_tasks(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.add_task("Task 2", "Description 2", "Medium", "Category 2", "2022-01-02")
        self.task_manager.add_task("Task 3", "Description 3", "Low", "Category 3", "2022-01-03")

        matching_tasks = self.task_manager.search_tasks("Nonexistent")
        self.assertEqual(len(matching_tasks), 0)

        matching_tasks = self.task_manager.search_tasks("Category 2")
        self.assertEqual(len(matching_tasks), 0)

    def test_categorize_task(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.categorize_task("Task 1", "New Category")
        self.assertEqual(self.task_manager.tasks[0].category, "New Category")

    def test_set_due_date(self):
        self.task_manager.add_task("Task 1", "Description 1", "High", "Category 1", "2022-01-01")
        self.task_manager.set_due_date("Task 1", "2022-02-01")
        self.assertEqual(self.task_manager.tasks[0].due_date, "2022-02-01")


if __name__ == '__main__':
    unittest.main()
