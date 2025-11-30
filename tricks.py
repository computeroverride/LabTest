result = map(int, ["1","2","3"]) #converts strings to integers

print(list(result))  # [1, 2, 3]
print(list(result))  # []  (already consumed)

######################################################################
import statistics

numbers = [1, 2, 3, 4]

statistics.mean(numbers)        # average
statistics.median(numbers)      # middle value
statistics.mode(numbers)        # most common value
statistics.stdev(numbers)       # standard deviation
######################################################################
my_dict = {"apple": 3, "orange": 5}

for key in my_dict:
    print(my_dict[key])