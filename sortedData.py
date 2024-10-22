import csv
import os

output_directory = '/home/bj2772798/TIDAL/'  # Replace with your desired path
csv_file_path = os.path.join(output_directory, 'unsorted_data.csv')
sorted_file_path = os.path.join(output_directory, 'sorted_data.csv')  # Update to include the directory

fplUnder150 = [22590, 30660, 38730, 46800, 
       54870, 62940, 71010, 79080]
fplUnder250 = [37650, 51100, 64550, 78000, 
       91450, 104900, 118350, 131800]

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

# Read the data from the original CSV file
with open('/home/bj2772798/TIDAL/unsorted_data.csv', mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)
print("Read data")
eligible = 0
# Sort the data based on the first column (index 0)
data.sort(key=lambda x: int(x[0]))
for row in data:
    if row:  # Ensure the row is not empty
            first_value = int(row[0])  # First column value
            second_value = int(row[1])  # Second column value
            third_value = int(row[2])
            
            # Adjust the condition based on your criteria
            # Assuming you want to check the first column against the FPL and the second column value
            if first_value <= fplUnder150[second_value - 1]:
                numBelowFPL150 += 1
                eligible = 1
            elif (first_value <= fplUnder250[second_value - 1]) and (third_value == 1):
                 numBelowFPL250 += 1
                 eligible = 1
            else:
                numAboveFPL += 1
                eligible = 0
            row.append(eligible)
print("Finished assigning eligibility")

numQualified = (numBelowFPL150 + numBelowFPL250) / len(data)

# Write the sorted data to a new CSV file in the specified directory

multiplier = 1

# Extract numeric values from the first column (index 0) for mean and median calculations

for row in data:
    if int(row[0]) <= fplUnder150[int(row[1]) - 1]:
        multiplier = 1
    elif int(row[0]) <= fplUnder250[int(row[1]) - 1] and int(row[2]) == 1:
        multiplier = 1
    else:
        multiplier = 1.25
    annualRate = numMonths * float(row[3]) * float(row[0]) * originalIncomePercentage * numQualified * multiplier
    annualRate = round(annualRate, 2)
    row.append(annualRate)
    totalRevenue += annualRate

with open('/home/bj2772798/TIDAL/sorted_data.csv', mode='w', newline='') as file:
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
