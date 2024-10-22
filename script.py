import csv
import random

a = 0
numPeople = 0
specialHardShip = 0
waterRate = 0
csv_file_path = '/home/bj2772798/TIDAL/unsorted_data.csv'
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    for x in range(0, 31000):
        a = random.randint(20000, 21112)
        numPeople = random.randint(1, 8)
        specialHardShip = random.randint(1, 10)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 13000):
        a = random.randint(21113, 54994)
        numPeople = random.randint(1, 8)
        specialHardShip = random.randint(1, 10)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 21279):
        a = random.randint(54995, 63571)
        numPeople = random.randint(1, 8)
        specialHardShip = random.randint(1, 10)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 120585):
        a = random.randint(63572, 72653)
        numPeople = random.randint(1, 8)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 156051):
        a = random.randint(72652, 81231)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 113491):
        a = random.randint(81232, 89808)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 113491):
        a = random.randint(89809, 98890)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.5, .9)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 56745):
        a = random.randint(98891, 107467)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.3, .6)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 28372):
        a = random.randint(107468, 116549)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.3, .6)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 28372):
        a = random.randint(116550, 125126)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.3, .6)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 14186):
        a = random.randint(125127, 133703)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.3, .6)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
    for x in range(0, 14186):
        a = random.randint(142786, 151868)
        numPeople = random.randint(1, 4)
        specialHardShip = random.randint(1, 25)
        waterRate = random.uniform(.3, .6)
        writer.writerow([a, numPeople, specialHardShip, waterRate])
print("done")
