import os
PATH=os.getcwd()+'/day_9/input.txt'

def load_and_convert_input(path):
    with open(path,'r') as file:
        input = file.readlines()
        return  [values.split() for values in input]

def calculate_prediction(values):
    values=[int(v) for v in values]
    calculated_values=[values]
    current_row_values=values
    while any(x!=0 for x in current_row_values):
        current_row_values=[current_row_values[i+1]-current_row_values[i] for i in range(len(current_row_values)-1)]
        calculated_values.append(current_row_values)
    return calculated_values

def calculate_next_value(predictions):
    last_values=[row[-1] for row in predictions]
    return sum(last_values)

input=load_and_convert_input(PATH)
print(sum([calculate_next_value( calculate_prediction(history_value)) for history_value in input]))