import random

class Generator():
    def __init__(self, sex: str):
        self.sex = sex 

    def full_name(self):
        if self.sex == "male":
            file_id = random.randint(1, 5)
            self.names_path = "NameGenerator/names/names/male/1.txt"
            self.surnames_path = f"NameGenerator/names/surnames/male/{file_id}.txt"
            with open(self.names_path, "r", encoding="UTF-8") as file:
                names = file.readlines()
                self.first_name = random.choice(names).strip()
            with open(self.surnames_path, "r", encoding="UTF-8") as file:
                surnames = file.readlines()
                self.surname = random.choice(surnames).strip()
            return f"{self.first_name} {self.surname}"
        elif self.sex == "female":
            raise RuntimeWarning("This function not working now!")
        else:
            raise ValueError("Sex must be'male' or 'female'")        