import random


class Family:
    new_id = 0

    def __init__(self):
        self.memberCount = random.randint(2, 7)
        self.members = []

        self.id = Family.new_id
        Family.new_id += 1

        # self._infectedMemberCount

    def add_a_member(self, member):
        self.members.append(member)

