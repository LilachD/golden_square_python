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
Organiser
- todo list
- diary
- phone book??
- add(entry)
​
    Diary
    - show all entries
    - count words
    - calculate reading time
​
        DiaryEntry
        - title / contact name / task
        - contents / mobile number
​
    Todo list
    - show incomplete tasks
    - show completed tasks
​
        todo
        - task
        - status
​
​
​
​
class Organiser:
    # User-facing properties:
    #  none??
    #   Diary: a list of DiaryEntry instances
    #   Phonebook: a list of strings representing phone numbers
    #   Todo_list: a list of ToDo instances
​
    def __init__(self):
        pass # No code here yet
​
    def add_diary(self, diary):
        # Parameters:
        #   diary: an instance of Diary 
        # Side-effects:
        #   Adds the diary to self._diary
        pass # No code here yet

    def add_todo_list(self, todo_list):
        # Parameters:
        #   todo_list: an instance of TodoList 
        # Side-effects:
        #   Adds the todo_list to self._todo_list
        pass # No code here yet
​
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet
​
​
class Track:
    # User-facing properties:
    #   title: string
    #   artist: string
​
    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet
​
    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet
​
3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.
​
# EXAMPLE
​
"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
​
4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.
​
# EXAMPLE
​
"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
​
Encode each example as a test. You can add to the above list as you go.
​
5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
​