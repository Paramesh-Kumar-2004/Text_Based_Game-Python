import random

weaponlist = ["M1014","AWM","AK47","SWORD","CAPTAIN_AMERICA_SHILD","ARROW"]


class char():
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.weapons = ["Mele"]
        self.add_weapon2 = []
        self.score = 0
        self.life = 3

    def add_weapon(self,weapon):
        self.weapons.append(weapon)

    def show_weapons(self):
        print(f"\nWeapon List : {self.weapons}")


def start():
    # name = input("Enter Your Name \n>")
    name = input("\nEnter Player Name : ")
    # print("Your Role Is Shooter!..\n")
    role = "Shooter"
    print()    
    player = char(name,role)
    wish(player)


def wish(char):
    print(f"\nHappy Journy : {char.name}")
    print(f"\nYour Role Is : {char.role}")
    print(f"\nYour Weapons : {char.weapons}")
    print("\nGame Started...")
    first(char)


def first(char):
    weapon = random.randint(0,len(weaponlist)-1)
    v = []
    # weapon = input("Select Weapon To Add In Weapons Bag : (Ex: M1014)\n>>> ")
    select_weapon = random.randint(0,len(weaponlist)-1)
    # print("\nOriginal Weapon :",weaponlist[select_weapon])
    weaponselectlist = {weaponlist[random.randint(0,len(weaponlist)-1)],weaponlist[select_weapon],weaponlist[random.randint(0,len(weaponlist)-1)]}
    s_weapon = input(f"Select Correct Weapon To Add Your Weapon List : {weaponselectlist}\n>>> ").upper()
    # print("VVVVVV : ",weaponselectlist,"PPPPPPP: ",s_weapon)
    if(weaponlist[select_weapon] == s_weapon):
        char.add_weapon(s_weapon)
        char.show_weapons()
        select_path(char)
    else:
        print("Wrong!... Play With Inbuild Weapon...")
        select_path(char)
    # first(char)


def select_path(char):
    path = input("\nSelect Your Path To Go : (Ex: Right Left)\n>>> ").lower()
    path_gifts = ["Dragon","treasure"]
    path_gifts2 = random.randint(0,len(path_gifts))-1
    if(path_gifts[path_gifts2] == "Dragon"):
        print("Dragon Appears...")
        attack_or_run(char)
        # print("Attack")
    elif(path_gifts[path_gifts2] == "treasure"):
        open_or_leave_treasure(char)
        # print("treasure")
    else:
        print("Select Correct One...")
        select_path(char)


def attack_or_run(char):
    option = input("Select Your Option \"Attack\" or \"Run\" \n>>> ").lower()
    if(option == "attack"):
        attack(char)
    elif(option == "run"):
        run(char)
    else:
        print("Invalid Choice... ",end=" ")
        print("Please Select Correct Path...")
        attack_or_run(char)        
        
        
def attack(char):
    attack1 = random.randint(0,5)
    fake_attack = {attack1,random.randint(0,5),random.randint(0,5)}
    # print(f"Original Value : {attack1}")
    print(f"Select Range To Run : {fake_attack}")
    attack2 = int(input(">>> "))
    if(attack1 == attack2):
        print("You Killed The Beast...")
        char.score+=1
        if(char.score == 0):
            win()
        select_path(char)
    elif(attack1 != attack2):
        print("Sorry! Beast Killed You...")
        print("You Lose 1 Life...")
        char.life-=1
        if(char.life == 0):
            lose()
        select_path(char)
    else:
        print("Enter Correct Value....")
        attack(char)
    # print("Score : ",char.score)
    # print("Life  : ",char.life)
    # print(char.weapons)


def run(char):
    run1 = random.randint(0,5)
    fake_run = {run1,random.randint(0,5),random.randint(0,5)}
    # print(f"Original Value : {run1}")
    print(f"Select Range To Run : {fake_run}")
    run2 = int(input(">>> "))
    if(run1 == run2):
        print("You Away From The Beast...")
        char.score+=1
        select_path(char)
    elif(run1 != run2):
        print("Sorry! Beast Catched You...")
        print("You Lose 1 Life...")
        char.life-=1
        select_path(char)
    else:
        print("Enter Correct Value....")
        run(char)
    # print(char.weapons)


def open_or_leave_treasure(char):
    print("You Got A Treasure...")
    open_leave = input("If You Want To \"Open\" Or \"Leave\" The treasure \n>>> ").lower()
    if(open_leave == "open"):
        # char.weaponlist
        p = random.randint(0,len(weaponlist)-1)
        vp = weaponlist[p]
        print(f"You Got New Gun... {vp}")
        print(f"Weapon List : {char.weapons}")
        # print(weaponlist[p])
        # print(vp)
        if((vp not in char.add_weapon2) and (vp in weaponlist)):
            char.add_weapon2.append(vp)
            
        # print(char.add_weapon2)
        # open_or_leave_treasure(char)
        select_path(char)
        
    elif(open_leave == "leave"):
        print("You Missed The Treasure...")
        select_path(char)


def lose():
    print("You Lose The Match...")
    print("Try Again...")
    match = input("You Want To Play Again (y/n) :").lower()
    if(match == 'y'):
        start()

def win():
    print("You Won The Match...")
    print("Play Again...")
    match = input("You Want To Play Again (y/n) :").lower()
    if(match == 'y'):
        start()


def show(char):
    print(f"Happy Gaming {char.name}")
    print(f"Your Role Is {char.role}")
    print(f"Your Weapons {char.weapons}")



start()

# if __name__ == "__main__":
    # start()
    # attack(player)  # Use the instance
    # attack(char)
    # wish(char)
    # player = char("Player1", "Shooter")  # Create an instance of char
    # first(player)
    # select_path(player)
    # open_or_leave_treasure(player)

