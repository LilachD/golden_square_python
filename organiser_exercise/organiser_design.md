Multi-Class Planned Design Recipe
​
1. Describe the Problem
As a user
So that I can record my experiences
I want to keep a regular diary
​
As a user
So that I can reflect on my experiences
I want to read my past diary entries
​
As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed
​
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
​
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
​
​
2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com
​

phoneNumberFinder -> Diary
bestEntryExctractor -> Diary
Diary -> DiaryEntry
TodoList -> Todo
        ​

​
​class Diary:
    def __init__(self):
        # starts a list for storing entries
        # returns nothing
        pass 

    def add(self, entry):
        # entry: an instance of DiaryEnrty
        # side-effects: adds entry to the list __init__ed
        pass

    def all(self):
        # returns the list of all entries

           
class DiaryEntry:
    def __init__(self, title, contents):
        # title: a string rep the title of the entry
        # contents: a string rep the contents of the entry
        pass
    
    def format(self):
        # returns a formatted string eg: "title: contents"
        pass


class PhoneNumberExtractor:
    def __init__(self, diary):
        # diary: an instance of Diary
        pass
    
    def extract():
        # returns a list of all valid phone numbers found in diary
        pass


class BestEntryFinder:
     def __init__(self, diary):
        # diary: an instance of Diary
        pass
    
    def extract(self, wpm, minutes):
        # wpm: an integer representing reading speed as words per minute
        # minutes: an integer rep the time in minutes a user has to read
        # returns the longest entry content that can read in its entirety given a time limit and reading speed

    def count_words(entry):
        # entry: an Entry object
        # returns the total number of words in the entry

class TodoList: # as previously
class Todo: # as previously

​
3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.
​
# EXAMPLE
​

​
4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.
​
# EXAMPLE
​

​
5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
​