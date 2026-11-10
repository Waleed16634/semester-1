# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music = {
  "Travis Scott" : ["Utopia", "Astroworld", "Days Before Rodeo"],
  "Don Toliver" : ["Love Sick", "Heaven Or Hell", "Life Of A Don"],
  "Drake" : ["Views", "For All The Dogs", "ICEMAN"]

# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist
  print(music["Travis Scott"][0])
