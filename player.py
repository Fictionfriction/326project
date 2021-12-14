import random


class Player:
    """
    A player in the maze game
    
    Atrributes:
        name (str): the player's name
        health (int): the health that a player has to get through the maze
        score (int): the player's score for completing the maze
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.help = 3
        
# (Jalen)
    def player_hurt(self):
        """
        Player will take damage if they take a wrong turn in the maze
        """
        self.health = self.health - 1
        self.check_health()
        print(f"you now have {self.health} health left!")
    
    def player_health(self):
        """
        Player will gain health depending on if they meet a certain condition
        """
        self.health = self.health + 1
        
    def check_health(self):
        """Check if player has lost all of their health
        """
        if self.health == 0:
            print("You're out of health!")
            exit()
            
    def check_name(self):
        """
        Checks if the name the player uses is 3 characters, if not game will 
        not run
        """
        if len(self.name) != 3:
            return(print("Please make sure name is 3 characters long!"))
        else:
            return self.name

filename = 'directions.txt'

# Chooses from a random list of options and puts it in a list (Jalen)
directions1 = ['LEFT','RIGHT','FORWARD']
count = 0
directions = ['END']

while count < 10:
    directions.insert(0,random.choice(directions1))
    count += 1
     
    
    
        
class Maze():
    """
    Creates the maze that the player has to go through 
    
    Atrributes:
        instance (int): creates an instance for the player
        path (str): the direction that a user chooses going on the path
    """
    
    def __init__(self, instance):
        self.instance = instance
        self.score = 0

# (Jalen)      
    def turns(self):
        """
        asks the player which direction it wants to go
        """
        while True:
            user_movement = input(f"Hello {self.instance.name}, which way would you like to go? ").upper()
            self.check_path(user_movement)
        
    def check_path(self, path):
        """Checks whether the user chose the right path or not in the maze

        Args:
            path ([string]): the direction the user chose
        """
        if len(directions) == 2:
            print(f"You've reached the end! Score: {self.score}")
            exit()
        elif path.upper() == directions[0]:
            del directions[0]
            self.score+=1
            self.check_moves()
        elif path.upper() == "HELP":
            if self.instance.help > 0:
                self.use_help()
            else:
                print("You do not have any more help left.")
        else:
            print("Wrong way!")
            self.score-=1
            self.instance.player_hurt()
    
    def check_moves(self):
        if directions[0] != 'END':
            print("You have ", len(directions) - 1, " more directions to go")
            
    def use_help(self):
        print("The correct path is: ", directions[0])
        self.instance.help -= 1
            

player1 = Player('Bob')
maze1 = Maze(player1)
maze1.turns()
 

        
    
            
        
