class Loan:
    #initialize name ana salary of a person
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

#this function checks eligibility of person for loan

    def check_eligibility(self):

        #exeption haldled
        try:
            # If salary less than 10000 exception occured
            if self.salary < 10000 :        
                raise ValueError(f"{self.name} : Sorry, You are not eligible for loan because your salary is less than 10,000.")
        except ValueError as e:
            print(e)            #print Exception message
        else :
            print(f"{self.name} are eligible for loan Now you can apply for loan.")

#first instance
person1 = Loan("Ankit",9000)            # Exception occured in this case 
person1.check_eligibility()

#Second instance
person2 = Loan("Sameer",12000)          # Exception not occured in this case
person2.check_eligibility()


    