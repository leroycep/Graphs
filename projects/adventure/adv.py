from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def turn_right(dir):
    if dir == 'n':
        return 'e'
    elif dir == 'e':
        return 's'
    elif dir == 's':
        return 'w'
    elif dir == 'w':
        return 's'

traversal_path = []

map = {}
map[player.current_room.id] = {exit:'?' for exit in player.current_room.get_exits()}

while True:
    start_room = player.current_room

    unexplored_exits = [exit for (exit, exit_room) in map[start_room.id].items() if exit_room == '?']
    if len(unexplored_exits) == 0:
        break
    else:
        exit = random.choice(unexplored_exits)
        traversal_path.append(exit)
        player.travel(exit)
        map[start_room.id][exit] = player.current_room.id
        if player.current_room.id not in map:
            map[player.current_room.id] = {exit:'?' for exit in player.current_room.get_exits()}
        map[player.current_room.id][turn_right(turn_right(exit))] = start_room.id


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

# Print an ASCII map
world.print_rooms(visited_rooms)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
