Class Design Recipe

1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

2. Design the Class Interface
class Name_Of_Class:
    # User-facing properties:

    def __init__(self, parameter):
        # Parameter: data_type, 
            representing:
        # Side effects:
        pass 

    def method_name_1(self, parameter):
        # Parameter: data_type,
        #   representing:   
        # Returns:
        # Side-effects:
        pass

    def method_name_1(self, parameter):
        # Parameter: data_type,
        #   representing:   
        # Returns:
        # Side-effects:
        pass


Steps 3 and 4 then operate as a cycle.

3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.

4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.