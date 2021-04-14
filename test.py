csv_file = open("data.csv", 'r')
file_content = csv_file.read()

lines = file_content.split('\n')

big_array = []
for line in lines:
    line_content = line.split(",")
    big_array.append(line_content)

print(len(big_array))

'''

array = [
    [ST001, Ahmed, 1990-01-01],
    [ST002, Ali, 1991-01-01],
    [ST003, Aishath, 1992-01-01]
]'''