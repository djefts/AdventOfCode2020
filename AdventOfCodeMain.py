"""

Code written by David Jefts
Problems are taken directly from https://adventofcode.com/2020

"""
import timeit
import inputs
import importlib
import glob

# dynamically import all solution files
modules = glob.glob('solutions/*.py')
for m in modules:
    m = m[10:-3]
    globals()[m] = importlib.import_module(m, 'solutions.' + m)

print("\t--- Day One ---")
start = timeit.default_timer()
sol1 = Day1.day1(inputs.day1)
stop = timeit.default_timer()
print("  Solution:", sol1)
print("  Time: ", stop - start, "\n\n")

print("\t--- Day Two ---")
start = timeit.default_timer()
sol2 = Day2.day2(inputs.day2)
stop = timeit.default_timer()
print("  Solution:", sol2)
print("  Time: ", stop - start, "\n\n")

print("\t--- Day Three ---")
start = timeit.default_timer()
sol3 = Day3.day3(inputs.day3)
stop = timeit.default_timer()
print("  Solution:", sol3)
print("  Time: ", stop - start, "\n\n")

print("\t--- Day Four ---")
start = timeit.default_timer()
sol4 = Day4.day4(inputs.day4)
stop = timeit.default_timer()
print("  Solution:", sol4)
print("  Time: ", stop - start, "\n\n")
