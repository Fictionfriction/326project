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
        instance.check_health()
        print(f"you now have {self.health} health left!")
    
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

        
class Maze():
    def __init__(self, instance):
        self.instance = instance
      
    def turns(self,count):
        """
        asks the player which direction it wants to go
        """
        # will likely remove high score
        self.count = count
        while True:
            user_movement = input(f"Hello {self.name},  Which way would you like to go?").upper()
            instance.check_path(user_movement)
        
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
            instance.player_hurt()

        

        
    
            
        
