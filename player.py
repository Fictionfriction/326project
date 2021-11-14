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
        self.health = self.health - 1
    
    def player_health(self):
        self.health = self.health + 1
        
    def check_name(self):
        if len(self.name) > 3:
            return(print("Please make sure name is 3 characters long!"))
        else:
            return self.name

filename = 'directions.txt'
class Maze():
    
    def __init__(self):
        self.directions = filename
        
    