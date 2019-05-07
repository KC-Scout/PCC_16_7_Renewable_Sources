import csv
import pygal

canada = {}
mexico = {}
united_states = {}

canada_list = []
mexico_list = []
united_states_list = []

year = 1976

with open('country_renewable_data.csv') as f:
    reader = csv.reader(f)
### Dictionary Code:    
    # ~ header = list(next(reader))#How to enumerate a list? 
    # ~ years = (header[20:60]) 
    # ~ for row in reader:
        # ~ if 'mexico' in (row['ï»¿Name'].lower()):
            # ~ print("Mexico")
            # ~ for k, v in row.items():
                # ~ if int(k) > 1976:
                    # ~ print(k, v)
        # ~ if 'canada' in (row['ï»¿Name'].lower()):
            # ~ print("Canada")
            # ~ for k, v in row.items():
                # ~ print(k,v)
        # ~ if 'united states' in (row['ï»¿Name'].lower()):
            # ~ print("United States")
            # ~ for k, v in row.items():
                # ~ print(k,v)
    for row in reader:
        if 'mexico' in row[0].lower():
            for col in row[20:60]:
                mexico[year] = float(int(col))/1000
                mexico_list.append(float(int(col))/1000)
                year += 1
                
    year = 1976
    f.seek(0)
    
    for row in reader:
        if 'canada' in row[0].lower():
            for col in row[20:60]:
                canada[year] = float(int(col))/1000
                canada_list.append(float(int(col))/1000)
                year += 1
                
            
    year = 1976
    f.seek(0)
        
    for row in reader:
        if 'united states' in row[0].lower():
            for col in row[20:60]:
                united_states[year] = (int(float(col))/1000)
                united_states_list.append(int(float(col))/1000)
                year += 1

line_chart = pygal.Line(x_label_rotation = -90)
line_chart.x_labels = map(str, range(1976, 2016))            
line_chart.add('Mexico', mexico_list)
line_chart.add('Canada', canada_list)
line_chart.add('US', united_states_list)
line_chart.render_to_file('line_chart.svg')

