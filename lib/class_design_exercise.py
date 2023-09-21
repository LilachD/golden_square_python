class TODO_List():
    # User-facing properties:

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def show_list(self):
        return self.task_list

    def mark_complete(self, task):
        if task not in self.task_list:
            raise Exception('Task not in list')
        self.task_list.remove(task)
        return 'Task marked as complete'


inst = TODO_List()
inst.add_task('do this')
inst.mark_complete('do this')
print(inst.show_list)
