"""
--- Part One ---
Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and
then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum
to 2020; what do you get if you multiply them together?


--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you
a second one if you can find three numbers in your expense report that meet
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?
"""


def matchingSum(a, b, goal):
    return a + b == goal


def matchingTriple(a, b, c, goal):
    return a + b + c == goal


def day1(expense_report):
    print('\033[1m' + "Report Repair" + '\033[0m')
    
    day1_input = expense_report.split("\n")
    # print(day1_input)
    p1 = day1_p1(day1_input)
    p2 = day1_p2(day1_input)
    return p1, p2


def day1_p1(day1_input):
    for i in range(len(day1_input) - 1):
        a = int(day1_input[i])
        for j in range(i, len(day1_input)):
            b = int(day1_input[j])
            if matchingSum(a, b, 2020):
                # print(a, b, a + b, a * b)
                return a * b
    return "Sum not found"


def day1_p2(day1_input):
    for i in range(len(day1_input) - 2):
        a = int(day1_input[i])
        for j in range(i, len(day1_input) - 1):
            b = int(day1_input[j])
            for k in range(j, len(day1_input)):
                c = int(day1_input[k])
                if matchingTriple(a, b, c, 2020):
                    # print(a, b, c, a + b + c, a * b * c)
                    return a * b * c
    return "Sum not found"
