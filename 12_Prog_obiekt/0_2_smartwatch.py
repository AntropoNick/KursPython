class Electronic():
    def __init__(self):
        print ("Jestem robotem")

class Watch(Electronic):
    def __init__(self):
        print ("Show time")
        super().__init__()

class Phone(Electronic):
    def __init__(self):
        print ("Call me")
        super().__init__()

class Smartwatch(Watch,Phone):
    def __init__(self):
        print ("This smartwatch is great")
        super().__init__()

handband=Smartwatch()