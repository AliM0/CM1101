rec = "Reception"
admin = "MJ & Simon's room"
tut = "Tutor's Office"
park = "Parking lot"
office = "General Office"

room_reception = {"name":rec, "exits": {"South":admin, "East": tut, "West": park}, 
"description":"""You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west."""}

room_admins = {"name": admin, "exits":{"north": rec}, "description":"""You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception."""}

room_tutor = {"name" : tut, "exits": {"west": rec}, "description":"""You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west."""}

room_parking = {"name" : park, "exits" : {"south": rec , "east": office}, "description":"""You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office."""}

room_office = {"name" : office , "exits" :{ "west": park}, "description":"""You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings."""}


rooms = {"Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office}

print(rooms["Reception"]["exits"]["South"])
