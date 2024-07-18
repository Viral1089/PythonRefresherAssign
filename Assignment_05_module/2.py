#custom Exeption Class for exeption raise in vote function
class VoterAgeException(Exception):
    #intialization of message
    def __init__(self, message):
        self.message = message


class Voter:
    #initialize voter name and age 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #this fuction checks for eligibility age of a voter it is under 18 it raise exeption
    def vote(self):
        #exeption handle
        try:
            if self.age < 18:
                raise VoterAgeException(f"{self.name}:Sorry, you are not eligible to vote.") #custom exeption class called
        except VoterAgeException as e:              
            print(e.message)    #print Exeption message
        else:
            print(f"{self.name} is eligible to vote.")  #print name if voter eligible for vote

#first instance
voter1 = Voter("John", 17)          #exeption occured
voter1.vote()

voter2 = Voter("Namnesh",22)        #exeption not occured
voter2.vote()

        
