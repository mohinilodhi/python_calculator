class animal:
    def speak(slf):
        print("animal speaks very well")

class dog(animal):
    def speak(self):
        print("dog barks")

class cat(animal):
    def speak(self):
        print("cat meaows")

class person:
    def speak(self):
        print("person speaks")

class petowners(dog, cat, person):
    pass

owner = petowners()
owner.speak()
print(petowners.mro())


    