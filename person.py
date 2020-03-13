class Person():

    def __init__(self, *args, **kwargs):
        self.name = ''
        self.surname = ''
    
    def setName(self, name):
        self.name = name

    def setSurname(self, surname):
        self.surname = surname
    
    def getUser(self):
        return self.name + " " + self.surname