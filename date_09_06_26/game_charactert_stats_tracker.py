class GameCharacter: 
    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("'name' must be a string.")
        if not name.strip():
            raise ValueError("'name' cannot be empty.")

        self._name = name
        self._health = 100
        self._mana = 50 
        self._level = 1
    
    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"Mana: {self.mana}"
        )

    @property
    def name(self):
        return self._name
    

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise TypeError("'health' must be a whole number.")
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value
        

    @property
    def mana(self):
        return self._mana
        
    @mana.setter
    def mana(self, value):

        if not isinstance(value, int):
            raise TypeError("'mana' must be a whole number.")

        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1 
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")