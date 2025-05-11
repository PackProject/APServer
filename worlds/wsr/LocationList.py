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



#       Location:                                             Type                 Category ID    Sport ID        
location_table = OrderedDict([
    #Swordplay Duel
    ("Swordplay Duel - First Win",                            ('Custom',            1,             1)),
    ("Swordplay Duel (Stamp) - Cliff-hanger",                 ('Stamp',             1,             1)),
    ("Swordplay Duel (Stamp) - Straight to the Point",        ('Stamp',             1,             1)),
    ("Swordplay Duel (Stamp) - Met Your Match",               ('Stamp',             1,             1)),
    ("Swordplay Duel (Stamp) - One-Hit Wonder",               ('Stamp',             1,             1)),
    ("Swordplay Duel (Stamp) - Last Mii Standing",            ('Impossible Stamp',  1,             1)),
    ("Swordplay Duel - Pro Status",                           ('Pro Status',        1,             1)),
    ("Swordplay Duel - Beat The Champion (Matt)",             ('Champion',          1,             1)),


    #Swordplay Speed Slice          
    ("Swordplay Speed Slice - First Win",                     ('Custom',            1,             2)),
    ("Swordplay Speed Slice (Stamp) - Slice and Dice",        ('Stamp',             1,             2)),
    ("Swordplay Speed Slice (Stamp) - Slicing Machine",       ('Stamp',             1,             2)),
    ("Swordplay Speed Slice (Stamp) - Psychic Slice",         ('Stamp',             1,             2)),
    ("Swordplay Speed Slice (Stamp) - Double Time",           ('Stamp',             1,             2)),
    ("Swordplay Speed Slice (Stamp) - A Cut Above",           ('Impossible Stamp',  1,             2)),
    ("Swordplay Speed Slice - Pro Status",                    ('Pro Status',        1,             2)),
    ("Swordplay Speed Slice - Beat The Champion (Matt)",      ('Champion',          1,             2)),

    #Swordplay Showdown            
    ("Swordplay Showdown - Complete Stage 1",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 2",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 3",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 4",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 5",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 6",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 7",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 8",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 9",                 ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 10",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 11",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 12",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 13",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 14",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 15",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 16",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 17",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 18",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 19",                ('Custom',            1,             3)),
    ("Swordplay Showdown - Complete Stage 20",                ('Custom',            1,             3)),
    ("Swordplay Showdown (Stamp) - Not a Scratch",            ('Stamp',             1,             3)),
    ("Swordplay Showdown (Stamp) - Sword Fighter",            ('Long Stamp',        1,             3)),
    ("Swordplay Showdown (Stamp) - Perfect 10",               ('Hard Stamp',        1,             3)),
    ("Swordplay Showdown (Stamp) - Swordmaster",              ('Long Stamp',        1,             3)),
    ("Swordplay Showdown (Stamp) - Untouchable",              ('Impossible Stamp',  1,             3)),
    ("Swordplay Showdown - Pro Status",                       ('Pro Status',        1,             3)),

    #Wakeboarding            
    ("Wakeboarding (Stamp) - Huge Air",                       ('Stamp',             2,             4)),
    ("Wakeboarding (Stamp) - Bag of Tricks",                  ('Stamp',             2,             4)),
    ("Wakeboarding (Stamp) - Smooth Landing",                 ('Stamp',             2,             4)),
    ("Wakeboarding (Stamp) - Master Carver",                  ('Stamp',             2,             4)),
    ("Wakeboarding (Stamp) - The Long Way Home",              ('Stamp',             2,             4)),
    ("Wakeboarding - Pro Status",                             ('Pro Status',        2,             4)),

    #Frisbee Dog            
    ("Frisbee Dog (Stamp) - Good Dog",                        ('Stamp',             3,             5)),
    ("Frisbee Dog (Stamp) - Balloon Animal",                  ('Stamp',             3,             5)),
    ("Frisbee Dog (Stamp) - A for Effort",                    ('Hard Stamp',        3,             5)),
    ("Frisbee Dog (Stamp) - Perfect Target",                  ('Hard Stamp',        3,             5)),
    ("Frisbee Dog (Stamp) - Golden Arm",                      ('Hard Stamp',        3,             5)),
    ("Frisbee Dog - Pro Status",                              ('Pro Status',        3,             5)),

    #Frisbee Golf
    ("Frisbee Golf - Complete Hole 1",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 2",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 3",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 4",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 5",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 6",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 7",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 8",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 9",                        ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 10",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 11",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 12",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 13",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 14",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 15",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 16",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 17",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 18",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 19",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 20",                       ('Custom',            3,             6)),
    ("Frisbee Golf - Complete Hole 21",                       ('Custom',            3,             6)),            
    ("Frisbee Golf - Get a par",                              ('Custom',            3,             6)),
    ("Frisbee Golf - Get a birdie",                           ('Custom',            3,             6)),
    ("Frisbee Golf - Get an eagle",                           ('Custom',            3,             6)),
    ("Frisbee Golf (Stamp) - Under Par",                      ('Stamp',             3,             6)),
    ("Frisbee Golf (Stamp) - Lucky Skip",                     ('Stamp',             3,             6)),
    ("Frisbee Golf (Stamp) - On a Roll",                      ('Hard Stamp',        3,             6)),
    ("Frisbee Golf (Stamp) - Hole in One",                    ('Stamp',             3,             6)),
    ("Frisbee Golf (Stamp) - Straight and Narrow",            ('Impossible Stamp',  3,             6)),
    ("Frisbee Golf - Pro Status",                             ('Pro Status',        3,             6)),

    #Archery            
    ("Archery (Stamp) - Bull Stampede",                       ('Stamp',             4,             7)),
    ("Archery (Stamp) - Sure Shot",                           ('Stamp',             4,             7)),
    ("Archery (Stamp) - Century Shot",                        ('Long Stamp',        4,             7)),
    ("Archery (Stamp) - A Secret to Everybody",               ('Hard Stamp',        4,             7)),
    ("Archery (Stamp) - Sharpshooter",                        ('Impossible Stamp',  4,             7)),
    ("Archery - Pro Status",                                  ('Pro Status',        4,             7)),

    #Basketball 3-Point Contest            
    ("3-Point Contest (Stamp) - Hot Streak",                  ('Stamp',             5,             8)),
    ("3-Point Contest (Stamp) - Bonus Plumber",               ('Stamp',             5,             8)),
    ("3-Point Contest (Stamp) - Quick Draw",                  ('Hard Stamp',        5,             8)),
    ("3-Point Contest (Stamp) - Hot Hand",                    ('Impossible Stamp',  5,             8)),
    ("3-Point Contest (Stamp) - Pure Shooter",                ('Impossible Stamp',  5,             8)),
    ("3-Point Contest - Pro Status",                          ('Pro Status',        5,             8)),

    #Basketball Pickup Game            
    ("Pickup Game (Stamp) - Triple Dip",                      ('Stamp',             5,             9)),
    ("Pickup Game (Stamp) - Rim Rattler",                     ('Stamp',             5,             9)),
    ("Pickup Game (Stamp) - Lights Out",                      ('Hard Stamp',        5,             9)),
    ("Pickup Game (Stamp) - Buzzer Beater",                   ('Hard Stamp',        5,             9)),
    ("Pickup Game (Stamp) - Hoop Hero",                       ('Impossible Stamp',  5,             9)),
    ("Pickup Game - Pro Status",                              ('Pro Status',        5,             9)),
    ("Pickup Game (Stamp) - Beat The Champion (Tommy)",       ('Champion',          5,             9)),

    #Table Tennis            
    ("Table Tennis Match (Stamp) - In Your Face",             ('Stamp',             6,             10)),
    ("Table Tennis Match (Stamp) - Back from the Brink",      ('Hard Stamp',        6,             10)),
    ("Table Tennis Match (Stamp) - Epic Rally",               ('Hard Stamp',        6,             10)),
    ("Table Tennis Match (Stamp) - Perfectly Matched",        ('Hard Stamp',        6,             10)),
    ("Table Tennis Match (Stamp) - Table Titan",              ('Impossible Stamp',  6,             10)),
    ("Table Tennis Match - Pro Status",                       ('Pro Status',        6,             10)),
    ("Table Tennis Match - Beat The Champion (Lucia)",        ('Champion',          6,             10)),

    #Table Tennis Return Challenge             
    ("Return Challenge (Stamp) - 50-pointer",                 ('Stamp',             6,             11)),
    ("Return Challenge (Stamp) - 100-pointer",                ('Hard Stamp',        6,             11)),
    ("Return Challenge (Stamp) - 200-pointer",                ('Impossible Stamp',  6,             11)),
    ("Return Challenge (Stamp) - Recycler",                   ('Impossible Stamp',  6,             11)),
    ("Return Challenge (Stamp) - Save Face",                  ('Impossible Stamp',  6,             11)),
    ("Return Challenge - Pro Status",                         ('Pro Status',        6,             11)),
             
    #Golf             
    ("Golf - Complete Hole 1",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 2",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 3",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 4",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 5",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 6",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 7",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 8",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 9",                                ('Custom',            7,             12)),
    ("Golf - Complete Hole 10",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 11",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 12",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 13",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 14",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 15",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 16",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 17",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 18",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 19",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 20",                               ('Custom',            7,             12)),
    ("Golf - Complete Hole 21",                               ('Custom',            7,             12)),
    ("Golf - Par",                                            ('Custom',            7,             12)),
    ("Golf - Birdie",                                         ('Custom',            7,             12)),
    ("Golf - Eagle",                                          ('Custom',            7,             12)),
    ("Golf (Stamp) - Under Par",                              ('Stamp',             7,             12)),
    ("Golf (Stamp) - Chip In",                                ('Stamp',             7,             12)),
    ("Golf (Stamp) - King of Clubs",                          ('Hard Stamp',        7,             12)),
    ("Golf (Stamp) - Ace of Clubs",                           ('Impossible Stamp',  7,             12)),
    ("Golf (Stamp) - Hole in One",                            ('Impossible Stamp',  7,             12)),
    ("Golf - Pro Status",                                     ('Pro Status',        7,             12)),         

    #Bowling 10 Pin             
    ("Bowling 10 Pin - First Strike",                         ('Custom',            8,             13)),
    ("Bowling Standard (Stamp) - Gobble Gobble",              ('Stamp',             8,             13)),
    ("Bowling Standard (Stamp) - Split Spare",                ('Stamp',             8,             13)),
    ("Bowling Standard (Stamp) - High Roller",                ('Hard Stamp',        8,             13)),
    ("Bowling Standard (Stamp) - Pin Dropper",                ('Hard Stamp',        8,             13)),
    ("Bowling Standard (Stamp) - Perfect Game",               ('Impossible Stamp',  8,             13)),
    ("Bowling Standard - Pro Status",                         ('Pro Status',        8,             13)),      

    #Bowling 100 Pin             
    ("Bowling 100-Pin - First Strike",                        ('Custom',            8,             14)),
    ("Bowling 100-Pin (Stamp) - Super Strike",                ('Stamp',             8,             14)),
    ("Bowling 100-Pin (Stamp) - Split Spare",                 ('Stamp',             8,             14)),
    ("Bowling 100-Pin (Stamp) - Off the Wall",                ('Stamp',             8,             14)),
    ("Bowling 100-Pin (Stamp) - Secret Strike",               ('Stamp',             8,             14)),
    ("Bowling 100-Pin (Stamp) - Pin Dropper",                 ('Hard Stamp',        8,             14)),
    ("Bowling 100-Pin - Pro Status",                          ('Pro Status',        8,             14)), 

    #Bowling Spin Control             
    ("Spin Control - First Strike",                           ('Custom',            8,             15)),
    ("Spin Control (Stamp) - One for All",                    ('Stamp',             8,             15)),
    ("Spin Control (Stamp) - Split Spare",                    ('Stamp',             8,             15)),
    ("Spin Control (Stamp) - Head First",                     ('Stamp',             8,             15)),
    ("Spin Control (Stamp) - English Major",                  ('Hard Stamp',        8,             15)),
    ("Spin Control (Stamp) - Pin Dropper",                    ('Hard Stamp',        8,             15)),
    ("Spin Control - Pro Status",                             ('Pro Status',        8,             15)),     

    #Power Cruising             
    ("Power Cruising (Stamp) - Ringmaster",                   ('Stamp',             9,             16)),
    ("Power Cruising (Stamp) - 5,000-Pointer",                ('Long Stamp',        9,             16)),
    ("Power Cruising (Stamp) - Power Cruiser",                ('Hard Stamp',        9,             16)),
    ("Power Cruising (Stamp) - Power Jumper",                 ('Stamp',             9,             16)),
    ("Power Cruising (Stamp) - Leisure Cruiser",              ('Long Stamp',        9,             16)),
    ("Power Cruising - Pro Status",                           ('Pro Status',        9,             16)),
             
    #Canoeing             
    ("Canoeing (Stamp) - Beginner License",                   ('Stamp',            10,             17)),
    ("Canoeing (Stamp) - Intermediate License",               ('Hard Stamp',       10,             17)),
    ("Canoeing (Stamp) - Expert License",                     ('Impossible Stamp', 10,             17)),
    ("Canoeing (Stamp) - Ducks in a Row",                     ('Stamp',            10,             17)),
    ("Canoeing (Stamp) - Cut the Red Tape",                   ('Impossible Stamp', 10,             17)),
    ("Canoeing - Pro Status",                                 ('Pro Status',       10,             17)),
             
    #Cycling             
    ("Cycling - Complete Stage 1",                            ('Custom',           11,             18)),
    ("Cycling - Complete Stage 2",                            ('Custom',           11,             18)),
    ("Cycling - Complete Stage 3",                            ('Custom',           11,             18)),
    ("Cycling - Complete Stage 4",                            ('Custom',           11,             18)),
    ("Cycling - Complete Stage 5",                            ('Custom',           11,             18)),
    ("Cycling - Complete Stage 6",                            ('Custom',           11,             18)),
    ("Cycling (Stamp) - Last Gasp",                           ('Stamp',            11,             18)),
    ("Cycling (Stamp) - First of Many",                       ('Stamp',            11,             18)),
    ("Cycling (Stamp) - 1-Stage Master",                      ('Long Stamp',       11,             18)),
    ("Cycling (Stamp) - 3-Stage Master",                      ('Long Stamp',       11,             18)),
    ("Cycling (Stamp) - 6-Stage Master",                      ('Long Stamp',       11,             18)),
    ("Cycling - Pro Status",                                  ('Pro Status',       11,             18)),
              
    #Skydiving             
    ("Skydiving (Stamp) - High Five",                         ('Stamp',            12,             19)),
    ("Skydiving (Stamp) - For the Birds",                     ('Hard Stamp',       12,             19)),
    ("Skydiving (Stamp) - Friends in High Places",            ('Stamp',            12,             19)),
    ("Skydiving (Stamp) - Camera Shy",                        ('Stamp',            12,             19)),
    ("Skydiving (Stamp) - 200-point Dive",                    ('Hard Stamp',       12,             19)),
    ("Skydiving - Pro Status",                                ('Pro Status',       12,             19)),
             
    #Island Flyover             
    ("Island Flyover - Progressive I-Point Group (1)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (2)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (3)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (4)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (5)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (6)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (7)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (8)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (9)",        ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (10)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (11)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (12)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (13)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (14)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive I-Point Group (15)",       ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (1)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (2)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (3)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (4)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (5)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (6)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (7)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (8)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (9)",  ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (10)", ('Custom',           12,             20)),
    ("Island Flyover - Progressive White Balloon Group (11)", ('Custom',           12,             20)),
    ("Island Flyover (Stamp) - Island Hopper",                ('Stamp',            12,             20)),
    ("Island Flyover (Stamp) - Pop Frenzy",                   ('Hard Stamp',       12,             20)),
    ("Island Flyover (Stamp) - Follow That Plane",            ('Stamp',            12,             20)),
    ("Island Flyover (Stamp) - Wuhu Tour Guide",              ('Impossible Stamp', 12,             20)),
    ("Island Flyover (Stamp) - Balloonatic",                  ('Impossible Stamp', 12,             20))
])

location_sort_order = {
    loc: i for i, loc in enumerate(location_table.keys())
}

location_groups = {
    'Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp' or data[0] == 'Hard Stamp' or data[0] == 'Long Stamp' or data[0] == 'Impossible Stamp'],
    'Normal Stamp': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
    'Hard Stamp': [name for (name, data) in location_table.items() if data[0] == 'Hard Stamp'],
    'Impossible Stamp': [name for (name, data) in location_table.items() if data[0] == 'Impossible Stamp'],
    'Long Stamp': [name for (name, data) in location_table.items() if data[0] == 'Long Stamp'],
    'Pro Status': [name for (name, data) in location_table.items() if data[0] == 'Pro Status'],
    'Champion': [name for (name, data) in location_table.items() if data[0] == 'Champion'],
    'Difficulty': [name for (name, data) in location_table.items() if data[0] == 'Difficulty'],
    'iPoint': [name for (name, data) in location_table.items() if data[0] == 'iPoint'],
    'Balloon': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
    'Custom': [name for (name, data) in location_table.items() if data[0] == 'Stamp'],
}