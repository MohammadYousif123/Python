import tkinter as tk
from tkinter import messagebox

# Story template with placeholders
story_template = """
Once upon a time in a faraway {place}, there lived a {adjective} {noun}.
This {noun} loved to {verb} every single day.
One day, while {verb_ing}, the {noun} found a mysterious {object}.
It turned out to be a {adjective_2} day, because finding a {object} meant that {noun} would have a big adventure!
"""

# Function to generate the story using GUI inputs
def generate_story_gui():
    """
    Function to generate the mad libs story from GUI inputs and display it in a message box.
    """
    inputs = {
        'place': place_entry.get(),
        'adjective': adjective_entry.get(),
        'noun': noun_entry.get(),
        'verb': verb_entry.get(),
        'verb_ing': verb_ing_entry.get(),
        'object': object_entry.get(),
        'adjective_2': adjective_2_entry.get()
    }

    # Use the story template and format it with user inputs
    story = story_template.format(
        place=inputs['place'],
        adjective=inputs['adjective'],
        noun=inputs['noun'],
        verb=inputs['verb'],
        verb_ing=inputs['verb_ing'],
        object=inputs['object'],
        adjective_2=inputs['adjective_2']
    )
    
    # Display the final story in a message box
    messagebox.showinfo("Your Mad Labs Story", story)

# Create the main application window
root = tk.Tk()
root.title("Mad Labs Python Project")
root.geometry("400x500")  # Set the size of the window

# Create labels and entry widgets for user inputs
place_label = tk.Label(root, text="Enter a place:")
place_label.pack()
place_entry = tk.Entry(root)
place_entry.pack()

adjective_label = tk.Label(root, text="Enter an adjective:")
adjective_label.pack()
adjective_entry = tk.Entry(root)
adjective_entry.pack()

noun_label = tk.Label(root, text="Enter a noun:")
noun_label.pack()
noun_entry = tk.Entry(root)
noun_entry.pack()

verb_label = tk.Label(root, text="Enter a verb:")
verb_label.pack()
verb_entry = tk.Entry(root)
verb_entry.pack()

verb_ing_label = tk.Label(root, text="Enter a verb ending in 'ing':")
verb_ing_label.pack()
verb_ing_entry = tk.Entry(root)
verb_ing_entry.pack()

object_label = tk.Label(root, text="Enter an object:")
object_label.pack()
object_entry = tk.Entry(root)
object_entry.pack()

adjective_2_label = tk.Label(root, text="Enter another adjective:")
adjective_2_label.pack()
adjective_2_entry = tk.Entry(root)
adjective_2_entry.pack()

# Create a button to generate the story
generate_button = tk.Button(root, text="Generate Story", command=generate_story_gui)
generate_button.pack()

# Run the Tkinter event loop
root.mainloop()
