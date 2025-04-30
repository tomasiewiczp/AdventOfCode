# task url: https://adventofcode.com/2021/day/8
import pandas as pd

def read_input_file(file_path):
    with open(file_path, "r") as read_hook:
        return [line.split() for line in read_hook.readlines() ]

def discover_coding(encoded_values):
    len_value_mapping = ((2,1), (4,4), (7,8), (3,7))
    decoded_values = {encoded_values[encoded_values.str.len() == leng].values[0]: value for leng, value in len_value_mapping } #found 2,3,4,7
    reversed_d = {v: k for k, v in decoded_values.items()}

    found_value = [value for value in encoded_values if len(value)==6 and not set(reversed_d[1]).issubset(set(value))][0] #found 6
    decoded_values[found_value] = 6 
    encoded_values = encoded_values[encoded_values != found_value]

    found_value = [value for value in encoded_values if len(value)==6 and not set(reversed_d[4]).issubset(set(value))][0] #found 0
    decoded_values[found_value] = 0
    encoded_values = encoded_values[encoded_values != found_value] 

    decoded_values[encoded_values[encoded_values.str.len() == 6].values[0]] = 9 #found 9
    reversed_d = {v: k for k, v in decoded_values.items()}

    found_value = [value for value in encoded_values if len(value)==5 and set(reversed_d[1]).issubset(set(value))][0] #found 3
    decoded_values[found_value] = 3
    encoded_values = encoded_values[encoded_values != found_value]

    found_value = [value for value in encoded_values if len(value)==5 and set(value).issubset(set(reversed_d[9]))][0] #found 5
    decoded_values[found_value] = 5
    encoded_values = encoded_values[encoded_values != found_value]
    decoded_values[encoded_values[encoded_values.str.len() == 5].values[0]] = 2 #found 2
    return decoded_values

signals = pd.DataFrame(read_input_file('input.txt'))
sum_value = 0
for row in signals.iterrows():
    output_str = ''
    decoded = {''.join(sorted(k)): v for k, v in discover_coding(row[1][:10]).items()}
    output_value = int(''.join([str(decoded[''.join(sorted(val))]) for val in row[1][11:]]))
    sum_value += output_value
print(sum_value)