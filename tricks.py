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
