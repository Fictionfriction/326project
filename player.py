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
    
    def player_hurt(self):
        """
        Player will take damage if they take a wrong turn in the maze
        """
        self.health = self.health - 1
    
    def player_health(self):
        """
        Player will gain health depending on if they meet a certain condition
        """
        self.health = self.health + 1
        
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

directions = ['LEFT','RIGHT','FORWARD','RIGHT','FORWARD','RIGHT','LEFT','LEFT',
              'RIGHT','LEFT','END']

def check_path(path):
    """Checks whether the user chose the right path or not in the maze

    Args:
        path ([string]): the direction the user chose
    """
    if len(directions) == 1:
        print("You've reached the end!")
    elif path.upper() == directions[0]:
        del directions[0]
    else:
        print("Wrong way!")
        Player.player_hurt()
        
class Maze():
    def __init__(self, directions):
        self.directions = directions
      
    def turns(self,count):
        """
        counts the amount of turns made, as well asks the player which direction it wants to go
        """
        self.count = count
        user_movement = input("Which way would you like to go?").upper()
        if user_movement == self.directions
        
    
        



        

        
    
            
        
