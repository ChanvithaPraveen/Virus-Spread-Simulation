from person import Person
from family import Family
import random


class Population:
    def __init__(self):
        self.people = []
        self.families = []
        self.adults = []
        self.children = []
        self.adultCount = 0
        self.manCount = 0
        self.childCount = 0
        self.essentialServiceCount = 40000

        for i in range(1000000):
            new_person = Person()
            new_person_age = getattr(new_person, 'age')
            new_person_id = getattr(new_person, 'id')
            if new_person_age >= 65:
                self.adultCount += 1
                self.adults.append(new_person_id)
            elif new_person_age <= 18:
                self.childCount += 1
                self.children.append(new_person_id)
            else:
                essential_prob = random.randint(1, 100)
                if 1 <= essential_prob <= 9 and self.essentialServiceCount != 0:
                    setattr(new_person, 'isEssentialService', True)
                    self.essentialServiceCount -= 1
                self.manCount += 1
                self.adults.append(new_person_id)
            self.people.append(new_person)

        self.create_families()

    def create_families(self):
        random.shuffle(self.adults)
        random.shuffle(self.children)
        children_in_families_count = 0
        # availablePeople = [i for i in range(1000000)]
        for i in range(100000):
            # print(f"No of People {len(self._people)}")
            new_family = Family()
            no_members = new_family.memberCount
            new_family_id = new_family.id

            adult_id = self.adults.pop()
            self.people[adult_id].add_to_a_family(new_family_id)

            no_members -= 1

            for j in range(no_members):
                random_no = random.randint(0, 99)
                if random_no <= 50 and len(self.children) != 0:
                    child_id = self.children.pop()
                    self.people[child_id].add_to_a_family(new_family_id)
                    children_in_families_count += 1
                else:
                    adult_id = self.adults.pop()
                    self.people[adult_id].add_to_a_family(new_family_id)

            self.families.append(new_family)


