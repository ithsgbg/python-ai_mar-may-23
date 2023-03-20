import csv

def map_to_tshirt_size(input_file, output_file):
    # Open input file for reading
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        # Open output file for writing
        with open(output_file, 'w', newline='') as csv_out:
            fieldnames = ['height', 'weight', 'chest_circ', 'tshirt_size', 'color']
            writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
            writer.writeheader()
            
            # Loop through each row in the input file
            for row in reader:
                # Extract necessary measurements and convert to integers
                height = int(row['stature'])
                weight = int(row['weightkg'])
                chest_circ = int(row['chestcircumference'])/10
                #waist_circ = int(row['waistcircumference'])

                
                # Map measurements to T-shirt size based on guidelines
                if chest_circ < 84: # and waist_circ < 26:
                    tshirt_size = '2X-Small'
                    color = 'pink'
                elif chest_circ < 90: # and waist_circ < 30:
                    tshirt_size = 'Extra Small'
                    color = 'yellow'
                elif chest_circ < 95: # and waist_circ < 34:
                    tshirt_size = 'Small'
                    color = 'red'
                elif chest_circ < 102: # and waist_circ < 38:
                    tshirt_size = 'Medium'
                    color = 'blue'
                elif chest_circ < 112: # and waist_circ < 42:
                    tshirt_size = 'Large'
                    color = 'lawngreen'
                elif chest_circ < 123: # and waist_circ < 46:
                    tshirt_size = 'X-Large'
                    color = 'green'
                elif chest_circ < 133: # and waist_circ < 50:
                    tshirt_size = 'XX-Large'
                    color = 'slategray'
                else:
                    tshirt_size = 'XXX-Large'
                    color = 'black'
                # Write the measurements and predicted T-shirt size to output file
                writer.writerow({
                    'height': height,
                    'weight': weight,
                    'chest_circ': chest_circ,
                    #'waist_circ': waist_circ,
                    'tshirt_size': tshirt_size, 
                    'color': color
                })
                
map_to_tshirt_size('./mar20/male.csv', './mar20/new_male.csv')
