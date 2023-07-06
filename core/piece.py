

class Piece:
    def __init__(self, color, postion):
        self.color = color
        self.position = postion
        self.has_moved = False
    
    def get_color(self):
        return self.color
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_position):
        self.position = new_position
        self.has_moved = True

    #Abstract class for children
    def is_valid_mode(self, new_position):      
        pass
        
        