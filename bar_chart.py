import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import drugs

# Some data
list_of_report = drugs.get_reports()

pain_relievers = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["12-17"]
alcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"]
tobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["12-17"]
marijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["12-17"]
cocaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["12-17"]

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Pain Relievers', 'Alcohol', 'Tobacco', 'Marijuana', 'Cocaine')
y_pos = np.arange(len(people))
performance = pain_relievers, alcohol, tobacco, marijuana, cocaine
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=0, align='center',
        color='green')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Number of people')
ax.set_title('The number of people (age 12-17) who used drugs in 2001')

plt.show()
