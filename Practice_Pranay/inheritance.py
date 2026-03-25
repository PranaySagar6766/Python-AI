class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some Sound"

    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def speak(self):
        return "woof"

class GuideDog(Dog):
    def __init__(self,name , owner):
        super().__init__(name)
        self.owner = owner

    def speak(self):
        return f"woof! I guide {self.owner}"

    def guide(self):
        return f"{self.name} is guiding {self.owner}"


g = GuideDog("Bruno" , "Anhad")
print(g.speak())
print(g.guide())
print(isinstance(g , Animal))