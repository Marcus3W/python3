# =================================================================================================== #

# SET OPERATIONS

"""
You can perform set operations on Python sets. These operations include:

- Union: returns a set containing all the elements of all the sets
- Intersection: returns a set containing the elements that exist in all of the sets
- Difference: returns a set containing the elements that only exist in the first set
- Symmetric Difference: returns a set containing the elements that only exist in one of the sets
"""

# =================================================================================================== #

# UNION

"""
The union of two sets is the set of all elements in both sets.
"""

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Checkpoint 1
new_song_data = {}

# Checkpoint 2
for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)

"""
Checkpoint 2 shows how to use the union operator to combine two sets. 

- The key, val in song_data.items() works by iterating through the key-value pairs in the song_data dictionary. 
- The song_tag_set = set(val) line converts the list of tags into a set. 
- The user_tag_set = set(user_tag_data[key]) line converts the list of user tags into a set. 
- The new_song_data[key] = song_tag_set | user_tag_set line combines the two sets using the union operator and -
  assigns the result to the new_song_data dictionary.
"""

# =================================================================================================== #

# INTERSECTION

"""
The intersection of two sets is the set of elements that exist in both sets.
"""

