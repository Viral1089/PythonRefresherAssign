#Create function to generate data randomly with python standard library

import random
import string

def generate_random_data(data_type, data_range, data_length):
    if data_type == "integer":
        return [random.randint(data_range[0], data_range[1]) for _ in range(data_length)]
    elif data_type == "float":
        return [random.uniform(data_range[0], data_range[1]) for _ in range(data_length)]
    elif data_type == "string":
        return [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=data_range)) for _ in range(data_length)]
    elif data_type == "choice":
        return [random.choices(data_range) for _ in range(data_length)]
    else:
        return None

print(generate_random_data("integer",(0,10),10))
print(generate_random_data("string",10,10))



