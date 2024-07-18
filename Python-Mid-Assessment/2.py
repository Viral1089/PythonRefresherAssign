#[1, “a”, 2, “b”, 3, “c”] filter digits and alphabets separately using inbuilt functions like map, filter or reduce

def Filter_Digits_And_Alphabets(input_list):
    #isinstance checks the type of object in list and filter on the isinstance function and append it if type of objects matches
    digits = list(filter(lambda x: isinstance(x,int),input_list))  
    alphabates = list(filter(lambda x: isinstance(x,str),input_list))
    print(digits)
    print(alphabates)

input_list = [1,"a",2,"b",3,"c"]    #input
Filter_Digits_And_Alphabets(input_list) #function call
