import os
import random
import monster_superclass as msc

def game_meny(inpt):
    """
        Prints out a pretty meny with a input.
    """
    print("*********************************************************")
    print(f"           {inpt}                                       ")
    print("*********************************************************")

def print_map(grid, map_Size):
    """
        Prints out the map with two loops.
        Arguments are the grid(dict) and map size(int).
    """
    for x in range(map_Size):
        for y in range(map_Size):
            print(grid[x,y], end=" ")
        print() 
    print("\n")
def create_map(map_Size):
    """
        Creates the map with 2 for-loops. 
        It will be a dict where the keys are the x and y pos
        and the value will be x.
        Returns the Dict.
    """
    grid_map = {}
    for x in range(map_Size):
        for y in range(map_Size):
            grid_map[(x,y)] = "x"
    return grid_map

def int_input(question):
    """
        Error-handling for int questions. Argument is a text string.
        This only works for meny where you can only answer 1, 2 or 3.
        Returns the right answer.
    """
    while True:
        try:
            user_input = int(input(question))
            if user_input < 4 and user_input > 0:
                return user_input
            else:
                os.system("cls")
                print("You make your choice by entering 1,2 or 3.")
        except ValueError:
            os.system("cls")
            print("You make your choice by entering 1,2 or 3.")
            int_input(question)
def accepted_Hero_Input(question):
    """
        Error-handling for y or n. 
        Will return the answer.
    """
    answer = str(input(question))
    answer = answer.lower()
    if answer == "y" or answer == "n":
        return answer
    else:
        print("Please enter y for yes or n for no.")
        accepted_Hero_Input(question)

def chance_50():
    """
        Randomize a number between 1-100.
        Returns 1 or 0 depending on the random.
    """
    rad_int = random.randint(1,100)
    if rad_int >= 50:
        return 1
    else:
        return 0

def place_Monster(grid_map):
    """
        Argument is the Map.
        Creates a monster room dict and the value will be 1 or 0.
        1 means there is a monster.
        Returns the monster room dict.
    """
    rooms = grid_map.keys()
    monster_room_dict = {}
    for room in rooms:
        i = chance_50()
        if i == 1:
            monster = spawn_Rate()
            monster_room_dict[room] = monster
    
    return monster_room_dict    

def spawn_Rate():
    rnd_int = random.randint(1,50)
    if rnd_int <= 20 and rnd_int > 1:
        return_Value = "Spider"
    elif rnd_int <= 35 and rnd_int > 21:
        return_Value = "Skeleton"
    elif rnd_int <= 45  and rnd_int > 36:
        return_Value = "Orc"
    else:
        return_Value = "Troll"      
    return return_Value    

game_meny("Welcome to MF.JFAM's Dungeon Run!")
#Userame will be linked to the game save.
#This will be updated in the last sprint.
username = str(input("What is your username?\n> "))

#While loop for Hero Choice.
while True:
    os.system("cls")
    game_meny(f"Welcome, {username}!")
    hero_Choice = int_input("What hero do you wanna play?\n1.Knight\n2.Wizard\n3.Thief\n> ")

    if hero_Choice == 1:
        print("--Knight--\nInitiative 5\nDurability 9\nAttack 6\nFlexibility 4\n"
        "\nThe knight's special ability is Shieldblock. Avoid damage on the first attack")
        answer = accepted_Hero_Input("Do you wanna play with the Knight? y/n \n>")
        hero = "Knight"
    
    if hero_Choice == 2:
        print("--Wizard--\nInitiative 6\nDurability 4\nAttack 9\nFlexibility 5\n"
        "\nThe wizard's special ability is Flash of Light. An 80% chance to escape from combat")
        answer = accepted_Hero_Input("Do you wanna play with the Wizard? y/n \n>")
        hero = "Wizard"
    
    if hero_Choice == 3:
        print("--Thief--\nInitiative 7\nDurability 5\nAttack 5 \nFlexability 7\n"
        "\nSpecial Ability: Critical Hit. The thief has 25% chance to do double damage with each attack.")
        answer = accepted_Hero_Input("Do you wanna play with the Thief? y/n \n>")
        hero = "Thief"
    if answer == "y":
        break

os.system("cls")
game_meny(f"Playing as {hero}!")

map_Choice = int_input("What map size do you wanna play?\n1.Small\n2.Medium\n3.Large\n> ")

#Map Size will decide if it should be a 4x4, 5x5 or 8x8 map.

if map_Choice == 1:
    map_Size = 4
if map_Choice == 2:
    map_Size = 5
if map_Choice == 3:
    map_Size = 8

#Create the map and saves it to grid_map
grid_map = create_map(map_Size)
os.system("cls")
game_meny(f"Playing as {hero}!")

monster_Room_Dict = place_Monster(grid_map)
print(monster_Room_Dict)
#While loop for
while True:
    right_input = ("1","2","3","4")
    
    start_pos_input = str(input("What corner you wanna start in?\n1.Top left\n2.Top right\n3.Bottom left\n4.Bottom right\n> "))
    
    if start_pos_input in right_input:
        #Sets the start pos, 4 diffrent cases.
        if start_pos_input == "1":
            start_pos_x = 0
            start_pos_y = 0
        
        if start_pos_input == "2":
            start_pos_x = 0
            start_pos_y = map_Size - 1
        
        if start_pos_input == "3":
            start_pos_x = map_Size - 1
            start_pos_y = 0
        
        if start_pos_input == "4":
            start_pos_x = map_Size - 1
            start_pos_y = map_Size - 1
        os.system("cls")
        break
    else:
        os.system("cls")
        print("You make your choice by entering 1, 2, 3 or 4")

# @ Symbol is for the hero, sets it to the start pos.
grid_map[start_pos_x,start_pos_y] = "@"
#Hero pos variable is for to check where the hero is.
hero_pos = [start_pos_x, start_pos_y]

#While loop for movement.
wrong_input = ""
while True:
    os.system("cls")
    print(wrong_input)
    wrong_input = ""
    print_map(grid_map,map_Size)

    #Open room will be an O.
    grid_map[hero_pos[0], hero_pos[1]] = "o"
    movement = str(input("Where do you wanna go?"))
    
    if movement == "w":
        hero_pos[0] = hero_pos[0] - 1
    elif movement == "s":
        hero_pos[0] = hero_pos[0] + 1
    elif movement == "d":
        hero_pos[1] = hero_pos[1] + 1
    elif movement == "a":
        hero_pos[1] = hero_pos[1] - 1
    elif movement == "q":
        break
    else:
        wrong_input = "Use W for up, A for left, D for right, S for down.\n"
    
    #If the hero walk too far down.
    if hero_pos[0] > map_Size - 1:
       wrong_input = "You cant go that way!\n"
       hero_pos[0] = hero_pos[0] - 1
    #If the hero walk too far up.
    if hero_pos[0] < 0:
        wrong_input = "You cant go that way!\n"
        hero_pos[0] = hero_pos[0] + 1
    #If the hero walk too far right.
    if hero_pos[1] > map_Size - 1:
        wrong_input = "You cant go that way!\n"
        hero_pos[1] = hero_pos[1] - 1
    #If the hero walk too far left.
    if hero_pos[1] < 0:
        wrong_input = "You cant go that way!\n"
        hero_pos[1] = hero_pos[1] + 1
    #Puts @ where the hero is.
    else:
        grid_map[hero_pos[0], hero_pos[1]] = "@"
        hero_pos_Tuple = (hero_pos[0],hero_pos[1])
        if hero_pos_Tuple in monster_Room_Dict:
            wrong_input = monster_Room_Dict[hero_pos[0],hero_pos[1]]