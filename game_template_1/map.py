
import string

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",
 
 "exits": {"south":"Admins", "east": "Tutor", "west": "Parking"}

}

room_admins = {
    "name": "MJ and Simon's room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""",

"exits":{"north": "Reception"}
    
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

"exits": {"west": "Reception"}}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    # ADD EXITS HERE!   
"exits" : {"south": "Reception" , "east": "Office"}

}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    # ADD EXITS HERE!
"exits" :{ "west": "Parking"}

}


            
rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}

'''print(rooms[a])'''

"""from string import punctuation
s= "dfdf/d.f/.df.df"
'''def strip_punctuation(s):
s= ''.join(char for char in s if char not in punctuation)'''
no_punc = ""
for char in s:
    if char not in punctuation:
        no_punc= char + no_punc"""

"""s= no_punc
     
print(s)"""
    
"""
#print(rooms[room_admins])
"""
"""for x in rooms:
    print(rooms["Reception"]["exits"][x])"""
"""
x={1,2,3,4}

y=2
if y in x:
    print("got it motherfuckers")
else:
    print("u got me fuckers")
#
print(rooms["Reception"]["exits"]["south"])
print(rooms["Reception"]["exits"])

#if rooms rooms["Reception"]["exits"]["north"] in rooms:

if "south" in rooms["Reception"]["exits"]:
    print(True)
else:
    print(False)
    
    if rooms.__contains__(rooms["Reception"]["exits"]["north"]):
        if rooms["Reception"]["exits"]["north"]==None:
            print(False)
        else:
            print(True)

    else:
        print(False)
#elif rooms["Reception"]["exits"]["north"] in rooms:
 #   print(True)

#
s = "dfdfdf.d,f.,df.,d.f,.,.,.,df,;d,';,',"
print("enter: ")
m = input("enter: ") 
m = m.strip() # the char method could be used by checking the 0 position to the first letter, and the check the last char to last letter of the word or the sentence

print(m.lower())





exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)

punctuations = """ '''!()-[]{};:'"\,<>./?@#$%^&*_~''' """
no_punc=""
#

for char in s:
    if char not in punctuations:
        no_punc= char + no_punc

s= no_punc
"""
