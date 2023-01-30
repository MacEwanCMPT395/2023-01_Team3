class LectureRoom:

    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity


# Tests
room533 = LectureRoom('11-533', 36)
room534 = LectureRoom('11-534', 36)
room560 = LectureRoom('11-560', 24)
room562 = LectureRoom('11-562', 24)
room564 = LectureRoom('11-564', 24)

ListOfRooms = [room533, room534, room560, room562, room564]

print(room533.id)
print(room533.capacity)

room533.capacity = 20
print(room533.capacity)

for rooms in ListOfRooms:
    print(rooms.id, rooms.capacity)
