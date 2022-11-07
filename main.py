from simulation import Simulation
import pandas as pd
import matplotlib.pyplot as plt

print("Simulating COVID-19 spread in a conceptual community")
print()
sim = Simulation()
simulation_days = int(input("Enter no of days to simulate : "))
sim.input()
print()
print("Please wait... Results will pop up soon..!")
sim.run(simulation_days)
data = sim.save_data()
print()
print("Data: ")
print (data)
print()


plt.figure("Daily Infected Patients count daily")
x = data.Day
y = data.DailyInfectedPatients
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Daily Infected Patients")
plt.title("Daily Infected Patients count daily")


plt.figure("Total Fatalities count daily")
x = data.Day
y = data.TotalFatalities
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Total Fatalities")
plt.title("Total Fatalities count daily")


plt.figure("Total Hospitalized count daily")
x = data.Day
y = data.TotalHospitalized
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Total Hospitalized")
plt.title("Total Hospitalized count daily")


plt.figure("Recovered People count daily")
x = data.Day
y = data.RecoveredPeople
plt.plot(x, y, color='red', linewidth = 0.5,
         marker='o', markerfacecolor='red', markersize=5)
plt.xlabel("Day")
plt.ylabel("Recovered People")
plt.title("Recovered People count daily")


plt.show()
