import csv
import os

###################
# Run this second #
###################

output_directory = '/home/bj2772798/TIDAL-Hackathon/'  # Replace with your desired path
csv_file_path = os.path.join(output_directory, 'unsorted_data.csv')
sorted_file_path = os.path.join(output_directory, 'sorted_data.csv')

# Uses Federal Poverty Levels from 2024
fplUnder150 = [22590, 30660, 38730, 46800, 
       54870, 62940, 71010, 79080]
fplUnder250 = [37650, 51100, 64550, 78000, 
       91450, 104900, 118350, 131800]

# Initializing variables
numBelowFPL150 = 0
numBelowFPL250 = 0
numAboveFPL = 0
waterCharge = 0
waterUsage = 0
originalIncomePercentage = .01
annualRate = 0
numMonths = 12
numQualified = 0
totalRevenue = 0
eligible = 0
multiplier = 1

def assistedPaymentProgamEquation(numMonths, waterRate, income, incomePercentage, numQualified, multipler):
    return numMonths * waterRate * income * incomePercentage * numQualified * multipler


# Read the data from the original CSV file
with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)
print("Read data")


# Sort the data based on income
data.sort(key=lambda x: int(x[0]))
for row in data:
    if row:  # Ensure the row is not empty
            income = int(row[0])
            numPeople = int(row[1])
            specialHardship = int(row[2])
            
            # Checks if person is eligible for lower water charge
            if income <= fplUnder150[numPeople - 1]:
                numBelowFPL150 += 1
                eligible = 1
            elif (income <= fplUnder250[numPeople - 1]) and (specialHardship == 1):
                 numBelowFPL250 += 1
                 eligible = 1
            else:
                numAboveFPL += 1
                eligible = 0
            row.append(eligible)
print("Finished assigning eligibility")

numQualified = (numBelowFPL150 + numBelowFPL250) / len(data)




for row in data:
    # Determines multiplier based on eligibility factors such as income and number of people in household
    if int(row[0]) <= fplUnder150[int(row[1]) - 1]:
        multiplier = 1
    elif int(row[0]) <= fplUnder250[int(row[1]) - 1] and int(row[2]) == 1:
        multiplier = 1
    else:
        multiplier = 1.25
    # 
    annualRate = assistedPaymentProgamEquation(numMonths, float(row[3]), float(row[0]), 
                    originalIncomePercentage, numQualified, multiplier)
    annualRate = round(annualRate, 2)
    row.append(annualRate)
    totalRevenue += annualRate

# Writes new sorted information into csv file, can then be used to assign water bills
with open(sorted_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    title = ["Income", "Household Members", "Special Hardship Determinant", "Water Usage", "Eligibility", "Annual Water Bill"]
    writer.writerow(title)
    writer.writerows(data)
print("Finished writing csv file")
     

values = [int(row[0]) for row in data if row]  # Convert to int and filter out empty rows

print("Population: ", len(values))
print("Above FPL: ", numAboveFPL)
print("Below 150 FPL: ", numBelowFPL150)
print("Below 250 FPL: ", numBelowFPL250)
print("Total Revenue: ", totalRevenue)

print("Sorting completed. The sorted data is saved in", sorted_file_path)
