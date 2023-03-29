ITERATIONS = 1000

with open('./mar29/Pet_Supplies.json', 'r') as in_file:
    with open(f'./mar29/Pet_Supplies_{ITERATIONS}.json', 'w') as out_file:
        for _ in range(ITERATIONS):
            out_file.write(in_file.readline())
