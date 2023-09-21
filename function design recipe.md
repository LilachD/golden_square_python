Fuction Design Recipe

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

    function name: contains_task

    Takes arguemnts: One string of text

    Returns: True if string contains '#TODO'. False otherwise.

    Side effects: error message for empty string, or non-string data argument

3. Create Examples as Tests

example:
given x
returns y
function_name(x) => y

4. Implement the Behaviour - write your code