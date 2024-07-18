#[“name512”, “same1example”, “joy18full”] replace the digits from string inside list

def RemoveDigitsFromString(input_list):
    result_list=[]
    for word in input_list:
        formatted_string= ''.join([ch for ch in word if not ch.isnumeric()])
        result_list.append(formatted_string)
    return result_list    

input_list = ["name512","same1example","Joy18full"]
print(RemoveDigitsFromString(input_list))