from my_data_pb2 import MyData

my_data = MyData()
my_data.id = 123
my_data.name = "Sensor Reading"
my_data.value = 25.5


## Un Comment & Demo this to show the importance of datatypes in Proto Buf
# my_data.id = "123"
# my_data.name = "Sensor Reading"
# my_data.value = 25.5

serialized_data = my_data.SerializeToString()
print(serialized_data)

# Save the data to a .bin file
with open("my_data.bin", "wb") as f:
    f.write(serialized_data)

print("Saving data to .bin file.")

# Read the data from the .bin file
with open("my_data.bin", "rb") as f:
    serialized_data = f.read()

my_data = MyData()
my_data.ParseFromString(serialized_data)

print(f"ID: {my_data.id}")
print(f"Name: {my_data.name}")
print(f"Value: {my_data.value}")