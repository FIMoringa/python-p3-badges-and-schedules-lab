def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append("Hello, my name is " + name + ".")
    return badges

def assign_rooms(names):
    rooms = []
    for name in names:
        rooms.append(f"Hello, {name}! You'll be assigned to room {names.index(str(name)) + 1}!")
    return rooms

def printer(names):
    for name in names:
        print(f"Hello, my name is {name}.")

    for name in names:
        print(f"Hello, {name}! You'll be assigned to room {names.index(str(name)) + 1}!")
