Class Design Recipe

1. Describe the Problem
    As a user
    So that I can keep track of my tasks
    I want a program that I can add todo tasks to and see a list of them.

    As a user
    So that I can focus on tasks to complete
    I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
    Class global variables: a TODO list of tasks
    Functionality:
    1. add task to list
    2. see the list of tasks
    3. mark tasks as complete and removes them from the list

class TODO_List()
    # User-facing properties:

    def __init__(self):
        # Parameters: None
        # Side effects: initializes a list of tasks
        pass 

    def add_tasks(self, task):
        # Parameter: a string
        #   representing:  tasks to be added to list
        # Returns: None
        # Side-effects: adds a string to the self.list
        pass

    def show_list(self):
        # Parameter: none  
        # Returns: the list of tasks to do
        # Side-effects: none
        pass

    def mark_complete(self, task):
        # Parameter: a string
        #   representing: task to be removed
        # Returns: a string telling user the task was removed
        #           or that the task wasn't in the list in the first place
        # Side-effects: removes a task from the self.list
        pass


Steps 3 and 4 then operate as a cycle.

3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.