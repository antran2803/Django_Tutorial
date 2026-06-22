class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        return "Some generic animal sound"
    def sleep(self):
        return f"{self.name} is sleeping."
    def info(self):
        return f"Animal_Name is a {self.name}."

class Dog(Animal): 
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "Woof!"
    def fetch(self):
        return f"{self.name} is fetching the ball."
    
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.sound())  # Output: Woof!


for ch in "python":
    if ch == "h":
        continue
    print(ch , end="")

for i in range(5):
    if i == 3:
        break
else:
    print("Done")