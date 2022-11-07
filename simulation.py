import random
from population import Population
import pandas as pd

class Simulation:

    def __init__(self):
        self.population = Population()
        self.day = 0
        self.infectedPatientCount = 0
        self.recoveredPatientCount = 0
        self.fatalitiesCount = 0
        self.hospitalizedPatientCount = 0
        self.dailyInfected = []
        self.totalHospitalizedPatient = []
        self.totalFatalities = []
        self.recoveredPeopleCount = []
        self.isWearAMask = False
        self.isTravelRestrictions = False
        self.wearAMaskStartDate = 0
        self.wearAMaskEndDate = 0
        self.travelReStart = 0
        self.travelReEnd = 0

    def input(self):
        x = input("Press 1 if you wants to apply wear mask law in a time period(press any key otherwise): ")
        if x=='1':
            print()
            self.wearAMaskStartDate = int(input("Enter the start day of wearing mask law that you need to apply: "))
            self.wearAMaskEndDate = int(input("Enter the end day of wearing mask law that you need to apply: "))
        else:
            pass
        
        print()
        y = input("Press 1 if you wants to apply travel restrictions in a time period (press any key otherwise): ")
        if y=='1':
            print()
            self.travelReStart = int(input("Enter the start day of travel restrictions that you need to apply:"))
            self.travelReEnd = int(input("Enter the end day of travel restrictions that you need to apply: "))
        else:
            pass

    def run(self, days):
        random_person = random.randint(0, 99999)
        self.population.people[random_person].isInfected = True
        self.population.people[random_person].infectedDay = 0
        self.infectedPatientCount = 1

        for self.day in range(days):
            daily_infected_patient_count = 0
            if self.day == 0:
                daily_infected_patient_count = 1
            
            if self.wearAMaskStartDate <= self.day <= self.wearAMaskEndDate :
                self.isWearAMask = True
            else: self.isWearAMask = False
            
            if self.travelReStart <= self.day <= self.travelReEnd :
                self.isTravelRestrictions = True
            else: self.isTravelRestrictions = False

            for person in self.population.people:
                family_status = False
                if person.isInAFamily:
                    for member in self.population.families[person.familyId].members:
                        if self.population.people[member].isInfected is True and self.population.people[member].isHospitalized is False and self.day - self.population.people[member].infectedDay <= 11:
                            family_status = True
                is_hospitalized = person.isHospitalized
                person.calculate_infection_probability(self.day, self.isWearAMask, self.isTravelRestrictions,
                                                       self.infectedPatientCount,family_status)
                person.update_state(self.day)
                if person.infectedDay == self.day and person.isInfected is True:
                    self.infectedPatientCount += 1
                    daily_infected_patient_count += 1
                if self.day == person.hospitalizedDay:
                    self.hospitalizedPatientCount += 1
                if person.fatalDay == self.day:
                    self.fatalitiesCount += 1
                if person.isFatal is False and person.isRecovered is True and person.recoveredDay == self.day:
                    self.recoveredPatientCount += 1
                    self.infectedPatientCount -= 1
                    if is_hospitalized is True:
                        self.hospitalizedPatientCount -= 1

            self.dailyInfected.append(daily_infected_patient_count)
            self.totalHospitalizedPatient.append(self.hospitalizedPatientCount)
            self.totalFatalities.append(self.fatalitiesCount)
            self.recoveredPeopleCount.append(self.recoveredPatientCount)

    def save_data(self):
        days = [i for i in range(0, self.day + 1)]
        dt = {'Day':days, 'DailyInfectedPatients': self.dailyInfected, 'TotalFatalities': self.totalFatalities,
              'TotalHospitalized':
                  self.totalHospitalizedPatient, 'RecoveredPeople': self.recoveredPeopleCount}
        data = pd.DataFrame(data=dt)
        data.to_csv('data.csv')
        return data
