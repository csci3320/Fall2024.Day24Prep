from prettytable import PrettyTable
import math
from pprint import pprint

string = "we the people of the united states"

frequency = {c : string.count(c) for c in string}

# print(frequency)

sorted_keys = sorted(frequency, key=frequency.get, reverse=True)
# print(sorted_keys)

sorted_frequency = [(k, frequency[k]) for k in sorted_keys]

table = PrettyTable()
table.add_column("Letters", sorted_frequency + ["Total bits:"])


# Calculate the size to store each letter if we use 8 bits (byte) plus the sum of all these totals
bit_8 = [frequency[k]*8 for k in sorted_keys]
table.add_column("8-bit", bit_8 + [sum(bit_8)])


# Calculate the size to store each letter if we use x bits  plus the sum of all these totals
bits_required = math.ceil(math.log2(len(sorted_keys)))
bit_x = [frequency[k]*bits_required for k in sorted_keys]
table.add_column(f"{bits_required}-bit", bit_8 + [sum(bit_x)])

print(table)


# Calculate the Huffman coding
steps = []
this_step = sorted_frequency.copy()
steps.append(this_step)

max_steps = 15
step_count = 0
while(step_count < max_steps and len(steps[-1]) > 1):
  print(f"Step {step_count}")
  this_step = steps[step_count].copy()

  this_step = sorted(this_step, key=lambda x: x[1], reverse=True)
  last = this_step[-1]
  second_last = this_step[-2]
  print(last)
  print(second_last)
  this_step = this_step[:-2] + [([second_last[0],last[0]], second_last[1] + last[1])]
  


  steps.append(this_step)
  step_count+=1


for row in steps:
  print(row)

print()
print()

# Now print the tree
last = steps[-1][0][0]
done = []
while len(last) > 0:
  temp = last.pop(0)
  if type(temp) == str:
    done += temp
  else:
    last += temp[0]
    last += temp[1]
  
print(done)

print("Done")



