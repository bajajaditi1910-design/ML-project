import csv

data = [
    {'name': 'Sanch', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2020},
    {'name': 'Sancit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2021},
    {'name': 'Sachit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2021},
    {'name': 'anchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2022},
    {'name': 'Sannchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 20213},
    {'name': 'Schit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2020},
    {'name': 'achit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2021},
    {'name': 'chit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2023},
    {'name': 'Ssanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2020},
    {'name': 'Saanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2022},
    {'name': 'Sancchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2022},
    {'name': 'Sanchiit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2023},
    {'name': 'Sanchitt', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2020},
    {'name': 'Sanchhit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2021},
    {'name': 'Sanccchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2025},
    {'name': 'Snhit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2020},
    {'name': 'Sht', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2022},
    {'name': 'hit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2023},
    {'name': 'Aanchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2024},
    {'name': 'Nchit', 'branch': 'COE', 'year': 2, 'cgpa': 9.1, 'enrollment year': 2022},    
]
with open('university_records.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'branch', 'year', 'cgpa', 'enrollment year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
with open('university_records.csv', 'r' ,newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)

        
