import random


class Person:
    new_id = 0

    def __init__(self):
        age_prob = random.randint(1, 100)
        if 1 <= age_prob <= 31:
            self.age = random.randint(65, 90)
        elif 31 < age_prob <= 51:
            self.age = random.randint(1, 18)
        else:
            self.age = random.randint(19, 64)

        self.id = Person.new_id
        Person.new_id += 1

        self.isInAFamily = False
        self.familyId = -1
        self.infectionProbability = 0
        self.isEssentialService = False
        self.isInfected = False
        self.isFatal = False
        self.fatalDay = -1
        self.infectedDay = -1
        self.isHospitalized = False
        self.hospitalizedDay = -1
        self.isRecovered = False
        self.recoveredDay = -1

    def add_to_a_family(self, family_id):
        self.isInAFamily = True
        self.familyId = family_id

    def calculate_infection_probability(self, day, wear_mask, travel_restrictions,total_count,family_status):
        self.infectionProbability = 0
        if self.isRecovered is False and self.isHospitalized is False and self.isFatal is False \
                and self.isInfected is False:
            if self.age <= 18:
                self.infectionProbability = random.randint(10, 20)/100
            elif self.age < 65:
                self.infectionProbability = random.randint(15, 40)/100
            else:
                self.infectionProbability = random.randint(35, 60)/100
            if self.isEssentialService is True:
                self.infectionProbability *= random.randint(30, 40)/100
            if self.isEssentialService is False and travel_restrictions is True:
                self.infectionProbability -= random.randint(15, 25)/100
            if wear_mask is True:
                self.infectionProbability -= random.randint(5, 10)/100
            if family_status is True:
                self.infectionProbability *= random.randint(40, 80) / 100

            if total_count < 1000:
                self.infectionProbability *= 2 / 100
            else :
                self.infectionProbability *= ((total_count/10000)+2)/100

    def update_state(self, day):
        days_after_infection = day - self.infectedDay
        if self.isInfected and self.isRecovered is False and self.isFatal is False:
            if 5 < days_after_infection < 15 and random.randint(0, 1) == 1 and self.isHospitalized is False:
                self.isHospitalized = True
                self.hospitalizedDay = day
            elif days_after_infection == 15:
                self.isHospitalized = False
                self.isRecovered = True
                self.recoveredDay = day
                self.infectedDay = -1
                self.hospitalizedDay = -1

        if self.isInfected is False and self.isRecovered is False and self.isFatal is False:
            random_infection = random.randint(1, 100)
            if random_infection <= self.infectionProbability * 100 and self.infectionProbability != 0:
                self.isInfected = True
                self.infectedDay = day

        if self.isFatal is False and self.isInfected is True and days_after_infection > 10:
            random_selection = random.randint(1,10000)
            if random_selection == 345:
                self.isFatal = True
                self.fatalDay = day

