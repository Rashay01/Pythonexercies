#Task1
def add_room(rooms, room_number, bed_type="Double", smoking=False):
  for room in rooms:
    if (room["room_number"] == room_number):
      room["bed_type"] = bed_type
      room["smoking"] = smoking
      return
  rooms.append({
      "room_number": room_number,
      "bed_type": bed_type,
      "smoking": smoking,
      "availability": True
  })


#Task2
def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
  for room in rooms:
    if (room["bed_type"] == preferred_bed_type
        and room["smoking"] == smoking_preference and room["availability"]):
      room["availability"] = False
      return 


#Task3
def list_available_rooms(rooms):
  return [room for room in rooms if room["availability"]]


#-----------------------------------------Testing----------------------------------------------
rooms = [{
    "room_number": 1,
    "bed_type": "Queen",
    "smoking": True,
    "availability": True
}, {
    "room_number": 2,
    "bed_type": "Single",
    "smoking": False,
    "availability": False
}, {
    "room_number": 3,
    "bed_type": "Double",
    "smoking": True,
    "availability": True
}, {
    "room_number": 4,
    "bed_type": "King",
    "smoking": False,
    "availability": True
}]

add_room(rooms, 5, "Queen", True)
add_room(rooms, 6)
add_room(rooms, 1)
print(rooms)

print()
print()

print(book_room(rooms))
print(book_room(rooms))
print(book_room(rooms))
print(book_room(rooms, "Queen", True))

print(rooms)

print()
print()
print(list_available_rooms(rooms))


# def book_room(rooms, preferred_bed_type="Double", smoking_preference=False):
# for room in rooms:
#   if (room["bed_type"] == preferred_bed_type
#       and room["smoking"] == smoking_preference and room["availability"]):
#     room["availability"] = False
#     return "room successfully booked"
# return f"rooms with {preferred_bed_type} and smoking: {smoking_preference} fully booked"