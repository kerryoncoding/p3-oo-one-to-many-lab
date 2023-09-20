class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all_pets = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def all(self):
        all_pets.append(self)
    
    @property
    def validate_pet_type(cls, pet_type):
        if pet_type not in cls.PET_TYPES:
            raise Exception("error")



class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return all_pets
    
    def add_pet(self, pet):
        pass

