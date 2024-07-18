#[1,2,3,1,3,4,6,5,3] get unique numbers from list with basic constructs

def Unique_Numbers(input_list):
    # using set method it returns set of unique digits and then list method converted it into a list
    return list(set(input_list))

input_list=[1,2,3,1,3,4,6,5,3]
print(Unique_Numbers(input_list))