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

class Maze():
    def __init__(self):
        self.directions = filename
            
        
