class Stack:
    def __init__(self):
        self.items = []
        print("Stack created")
    def push(self, data):
        self.items.append(data)
        print("Pushed: ", data)
    def pop(self):
        return self.items.pop()    
    def is_empty(self):
       return self.items == []  
    def peek(self):
        return self.items[len(self.items)-1]   
    def size(self):
        return len(self.items)




# arr = Stack() # instance of Stack class or object

# arr.push("Mango");
# print(arr.size());
# arr.push("Apple");
# print(arr.size());
# arr.push("Banana");
# print(arr.size());
# print(arr.is_empty());

# print(arr.peek());
# print(arr.pop());



