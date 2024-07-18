import math               #importing  math module to do some mathematical operations

class Arithematics:
    #initialization of list
    def __init__(self,list_of_numbers):
        self.list_of_numbers = list_of_numbers

#calculating average 
    def avg(self):
        return sum(self.list_of_numbers)/len(self.list_of_numbers)

#Calculating mean       
    def mean(self):
        return self.avg()       #mean is equal to the avg so output of avg is output of mean.

#Calculating Mode
    def mode(self):
        frequency = {}          #store frequency of each unique number in list_of_numbers
        for i in self.list_of_numbers:
            frequency[i] = self.list_of_numbers.count(i)
        #number having maximum frequency is called mode
        mode = max(frequency, key=frequency.get)
        return mode

#calculating Standard deviation
    def Standard_deviation(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.list_of_numbers) / len(self.list_of_numbers)
        return math.sqrt(variance)

#list of numbers as a input for our test 
list_of_numbers = [1,2,1,2,1,2,1,2,1,3,4,5,6,7,8,4,3,2,1,7,8,9]

calculate = Arithematics(list_of_numbers)
print(f"Average of the Numbers is: {calculate.avg()}")
print(f"Mean of the Numbers is: {calculate.mean()}")
print(f"Mode of the Numbers is: {calculate.mode()}")
print(f"Standard Deviation of the Numbers is: {calculate.Standard_deviation()}")