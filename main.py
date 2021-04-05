import csv

filepath = 'input.txt'

#EventID | Time | Latitude | Longitude | Depth/km | Author | Catalog | Contributor | ContributorID | MagType | Magnitude | MagAuthor | EventLocationName
# latitude
# longitude
# magnatude
# depth
fields = ['lat','long','mag','depth']
data = ['','','','']
main_data = []
with open('data_output.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            split = line.split('|')
            data[0] = split[2]
            data[1] = split[3]
            data[2] = split[10]
            data[3] = split[4]
            csvwriter.writerow(data) 
            line = fp.readline()
            cnt += 1
    