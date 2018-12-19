import csv
import matplotlib.pyplot as plt

filename = 'Video Game Sale Visualization.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    genres = []
    global_sales = []
    for row in reader:
        genres.append(row[4])
        global_sales.append(row[10])
    print(genres)
    print(global_sales)

srt_sales = sorted(global_sales)
srt_genres = sorted(genres)

action_values = []
for i in range(len(srt_genres)):
    if srt_genres[i] == "Action":
        action_values.append(srt_sales[i])

def get_sum_values(genre, values):


for x in x_something:
    get_sum_values()

print(action_values)





fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(genres, c='blue')
genres.sort()
global_sales.sort()
plt.title('Video Game Sales Per Genre', fontsize=24)
plt.xlabel('Sales', fontsize=16)
plt.ylabel('Genre', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
