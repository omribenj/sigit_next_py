class Animal:
    zoo_name = "Hayaton"
    def __init__(self, name, hanger=0):
        """
        initializer for Animal class
        :param name: the name of the animal
        :type name: str
        :param hanger: the hanger level of the animal
        :type hanger: int
        """
        self._name = name
        self._hanger = hanger
    
    def get_name(self):
        """
        function returns the name of the animal
        :return:the name of the animal
        :rtype: str
        """
        return self._name
    
    def is_hungry(self):
        """
        fucntion to tell if the animal is hangry, its hangry if the hanger is bigger than 0
        :return:if the animal is hangry
        :rtype: boolean
        """
        return self._hanger > 0
    
    def feed(self):
        """
        reduces the hanger by 1
        """
        self._hanger -= 1

    def talk(self):
        pass


class Dog(Animal):
    """
    class that represents a dog, extends Animal
    """
    def talk(self):
        print("woof woof")
    
    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    """
    class that represents a Cat, extends Animal
    """
    def talk(self):
        print("meow")
    
    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    """
    class that represents a Skunk, extends Animal
    """
    def __init__(self, name, hanger=0, stink_count=6):
        super().__init__(name, hanger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")
    
    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    """
    class that represents a Unicorn, extends Animal
    """
    def talk(self):
        print("Good day, darling")
    
    def sing(self):
        print("I'm not your toy...")

class Dragon(Animal):
    """
    class that represents a Dragon, extends Animal
    """
    def __init__(self, name, hanger=0, color="Green"):
        super().__init__(name, hanger)
        self._color = color

    def talk(self):
        print("Raaaawr")
    
    def breath_fire(self):
        print("$@#$#@$")

def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("keith", 7), Dragon("Lizzy", 1450), Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80), Dragon("McFly", 80)]
    for animal in zoo_lst:
        if animal.is_hungry(): print(animal.__class__.__name__, animal.get_name())
        # feed the animal until not hungry
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        # do the special function for the Animal
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal,Cat):
            animal.chase_laser()
        elif isinstance(animal,Skunk):
            animal.stink()
        elif isinstance(animal,Unicorn):
            animal.sing()
        elif isinstance(animal,Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)

if __name__ == "__main__":
    main()