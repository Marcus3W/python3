"""
Sets


A set object can be created in two ways. You can use curly braces to create an empty set, like this: {}.

You can also pre-populate a set with values by passing a list to the set() function, like this:

my_set = set([1, 2, 3])   ------->   This will create a set with the values [1, 2, 3].

"""

# Example 1

music_genres = {"Pop", "Rock", "Jazz", "Pop", "R&B", "Rock", "Disco", "Pop"}
print(music_genres)

# Example 2

video_genres = set(["Action", "Comedy", "Drama", "Action", "Comedy", "Thriller", "Comedy"])
print(video_genres)


"""
It's worth noting that a set from a list with duplicate elements will only contain one of each element.

See and example below:
"""
multiple_set = {"Pop", "Rock", "Jazz", "R&B", "Disco", "Pop", "Rock", "Disco", "Pop"}
print(multiple_set) # will print {'Pop', 'Rock', 'Jazz', 'R&B', 'Disco'}


"""
You are also able to any combination of data types in a set, including strings, integers, and floats.

See an example below:
"""
random_data_types = {1, 2.0, "three", (4, 5, 6)}
print(random_data_types) # will print {1, 2.0, 'three', (4, 5, 6)}


"""
you can create an empty set using the set() function.
"""
empty_set = set()


"""
List comprehensions can also be used to create sets.
"""
items = ["apple", "orange", "banana", "apple", "apple", "orange"]
fruit_basket = {category for category in items if category == "apple" or category == "orange"}
print(fruit_basket) # will print {'orange', 'apple'}

# =================================================================================================== #

# Working exmaples

genre_results = [
                'rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 
                 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 
                 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 
                 'pop', 'rap', 'latin'
                ]

# Checkpoint 1
survey_genres = set(genre_results)
print(survey_genres)

# Checkpoint 2
survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)


# =================================================================================================== #

# ADDING ELEMENTS TO A SET

"""
You can add elements to a set using the .add() method.

See an example below:
"""

# Create a set to hold the song tags
song_tags = {'Country', 'Pop', 'R&B', 'Hip-Hop'}

# Add a new tag
song_tags.add('Jazz')
song_tags.add('Rock')

# Print the set
print(song_tags) # will print {'Country', 'Pop', 'R&B', 'Hip-Hop', 'Jazz', 'Rock'}


"""
You can also add multiple elements to a set using the .update() method.

See an example below:
"""

# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}

# Add multiple tags
other_tab = {'pop', 'rock', 'alternative', 'folk'}
song_tags.update(other_tab)

# Print the set
print(song_tags) # will print {'folk', 'rock', 'country', 'alternative', 'pop', 'acoustic'}

"""
Notes:
- None of these methods will add a duplicate element to a set.
- A Frozenset cannot be changed, so you cannot add elements to a frozenset.
- Sets and frozensets containers are unordered, so you cannot assume that the elements will be in a particular order.
"""

# Exmaple 1

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Checkpoint 1
tag_set = set(song_data['Retro Words'])

# Checkpoint 2
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

# or tag_set.update([user_tag_1, user_tag_2, user_tag_3])

# Checkpoint 3
song_data = {'Retro Words': tag_set}
print(song_data)


# =================================================================================================== #

# REMOVING ELEMENTS FROM A SET

"""
You can remove elements from a set using the .remove() method or the .discard() method.

See an example below:
"""

# .remove() method

song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}

# Remove an existing element
song_tags.remove('folk')
print(song_tags)

# Try removing a non-existent element - this will raise an error
# song_tags.remove('fiddle')


# .discard() method - No error is raised if the element does not exist

# Given a list of song tags
song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}

# Try removing a non-existent element but with the discard method
song_tags.discard('guitar')
print(song_tags)

# Try removing a non-existent element but with the discard method
song_tags.discard('fiddle')
print(song_tags)


# =================================================================================================== #

# Working Example:
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

tag_set.discard('onion')
tag_set.discard('helloworld')
tag_set.discard('spam')

song_data_users = {'Retro Words' : tag_set}


# =================================================================================================== #

# FINDING ELEMENTS IN A SET

"""
You can check if an element is in a set using the in keyword.

See an example below:
"""

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 
                'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 
                'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 
                'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 
                    'horrible', 'electric', 'mushroom', 'shed']}

# Checkpoint 1
tag_set = set(song_data_users['Retro Words'])

# Checkpoint 2
bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)

# Checkpoint 3
for tag in bad_tags:
  if tag in tag_set:
    tag_set.discard(tag)

# Checkpoint 4
song_data_users = {'Retro Words' : tag_set}
print(song_data_users)

