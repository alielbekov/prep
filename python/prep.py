# Data types
import asyncio
import time

"""Create a variable named "data" and assign it a dictionary with the following key-value pairs:

"text": "Hello, World!"
"integer": 42
"floating_point": 3.14
"complex_number": 2 + 3j
"sequence_list": ["apple", 1, 3.14, True]
"sequence_tuple": ("banana", 2, 2.71)
"sequence_range": range(1, 6)
"mapping_dict": {"name": "John", "age": 25, "is_student": True}
"set_values": {1, 2, 3, 4, 5}
"frozen_set_values": frozenset({5, 6, 7})
"boolean_value": False
"binary_bytes": bytes([0, 1, 2, 3, 4])
"binary_bytearray": bytearray([5, 6, 7, 8])
"none_value": None
Print the value of "text" from the "data" dictionary.

Perform an arithmetic operation (e.g., addition, subtraction) using the "integer" and "floating_point" values. Print the result.

Access the second element of the "sequence_list" and print it.

Check if the "mapping_dict" contains the key "name". Print the result.

Add a new key-value pair to the "mapping_dict" with the key "city" and the value "New York".

Check if the value 4 is present in the "set_values". Print the result.

Convert the "sequence_range" to a list and print it.

Perform a logical operation (e.g., AND, OR) using the "boolean_value" and the result from step 7. Print the result.

Concatenate the "binary_bytes" and "binary_bytearray" objects and print the result.
"""
data = {"text": "hello world",
        "integer": 42,
        "floating_point":3.14,
        "complex_number": 2+3j,
        "sequence_list": ["apple",1, 3,14, True],
        "sequence_tuple": ("banana", 2, 2.71),
        "sequence_range": range(1, 6),
        "mapping_dict": {"name": "John", "age": 25, "is_student": True},
        "set_values": {1, 2, 3, 4, 5},
        "frozen_set_values": frozenset({5, 6, 7}),
        "boolean_value": False,
        "binary_bytes": bytes([0, 1, 2, 3, 4]),
        "binary_bytearray": bytearray([5, 6, 7, 8]),
        "none_value": None
        }

print(data["text"])

float_data, integer_data = data["floating_point"],  data["integer"]
print(float_data+integer_data*10-13, "= 410,14")
print("second element of the list ", data["sequence_list"][1], " !")
print("it contains key 'name' ?", ("name" in data))
data["city"] = "New York"
print("is 4 present in set values? ", (4 in data["set_values"]))
seq_range = data["sequence_range"]
list_seq_range = list(seq_range)
print("list_seq_range " , list_seq_range)
print(data["boolean_value"] and True)

binary_bytes = data["binary_bytes"] 
binary_bytearray = data["binary_bytearray"]

binary_bytes_string = str(binary_bytes)
binary_bytearray_string  = str(binary_bytearray)
print(binary_bytes_string+ binary_bytearray_string)



########################################################################
#Context Manager

#1. with context as context:

with open("hello.txt", mode="w") as file:
    # whatever that comes after wite .___enter__() ed and most of the time an object is returned.
    # opens and writes a file
    file.write("Hello, World!")
with open("hello.txt", mode="r") as file:
    # opens a file in read mode and prints it as  a list.
    x = file.readlines()
    print(x)
    
# Iterator
for i in range(100):
    if i%5==0 :
        print(i)
        
# Operator

def count_to_five():
    print("operator start")
    for i in range(1, 6):
        print(i)


# implement async IO
async def count():
    print("1")
    await asyncio.sleep(1)
    print("2")



count()



count_to_five()
