from collections import OrderedDict

#
#   Type Definitions:
#
#   Stamp - Stamp collected from completing some task in a sport
#   Hard Stamp - Stamp that is deemed too hard for casuals to reliably get. These can be removed in logic in settings
#   Long Stamp - Stamp that is deemed too much of a grind to get. These can be removed in logic in settings
#
#   Pro Status - Getting pro status in a sport
#   Champion - Beating the champion in a sport
#   Difficulty - Unlocking the next difficulty in a sport
#   Level - Unlocking the next level in a sport.
# 
#   iPoint - I-Point in Island Flyover (only half ever required)
#   Balloon - White Balloon in Island Flyover (only half ever required)
#
#   Custom - Custom locations added for the randomizer. Example could be getting your first win in Speed Slice
#



#       Location:                              Type               Category ID    Sport ID        
location_table = OrderedDict([
























])

location_sort_order = {
    loc: i for i, loc in enumerate(location_table.keys())
}

location_groups = {
    'Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
    'Normal Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp' or data[0] == 'Hard Stamp' or data[0] == 'Long Stamp'],
    'Hard Stamp': [name for (name, data) in location_table.items() if data[0] == 'Hard Stamp'],
    'Long Stamp': [name for (name, data) in location_table.items() if data[0] == 'Long Stamp'],
    'Pro Status': [name for (name, data) in location_table.items() if data[0] == 'Pro Status'],
    'Champion': [name for (name, data) in location_table.items() if data[0] == 'Champion'],
    'Difficulty': [name for (name, data) in location_table.items() if data[0] == 'Difficulty'],
    'iPoint': [name for (name, data) in location_table.items() if data[0] == 'iPoint'],
    'Balloon': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
    'Custom': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
}