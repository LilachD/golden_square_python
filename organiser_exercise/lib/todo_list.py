class TodoList:
    def __init__(self):
        self.task_list = []

    def add(self, todo):
        self.task_list.append(todo)

    def incomplete(self):
        return [task for task in self.task_list if task.complete == False]

    def complete(self):
        return [task for task in self.task_list if task.complete == True]

    def give_up(self):
        for task in self.task_list:
            task.mark_complete()