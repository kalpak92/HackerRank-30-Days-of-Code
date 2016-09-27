class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print ("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    
    def yearPasses(self):
        self.age += 1
    
    def amIOld(self):
        if self.age < 13:
            print ('You are young.')
        elif self.age in range(13,18):
            print ('You are a teenager.')
        else:
            print ('You are old.')