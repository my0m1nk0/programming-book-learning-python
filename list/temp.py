from node import Node

temp = Node(99)

print("Init Data is =>",temp.get_data())
temp.set_next(100)
print("Next Data is =>",temp.get_next())
temp.set_data(55)
print("Set Data is =>",temp.get_data())


