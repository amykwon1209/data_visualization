import numpy as np
import matplotlib.pyplot as plt
import drugs

# Some data
list_of_report = drugs.get_reports()

alcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"]
tobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["12-17"]
marijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["12-17"]
cocaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["12-17"]

alcohol_cure = list_of_report[0]["Totals"]["Alcohol"]["Perceptions of Risk"]["12-17"]
tobacco_cure = list_of_report[0]["Totals"]["Tobacco"]["Perceptions of Risk"]["12-17"]
marijuana_cure = list_of_report[0]["Totals"]["Marijuana"]["Perceptions of Risk"]["12-17"]
cocaine_cure = list_of_report[0]["Totals"]["Illicit Drugs"]["Need Treatment Past Year"]["12-17"]


N = 4
total = (alcohol, tobacco, marijuana, cocaine)
cure = (alcohol_cure, tobacco_cure, marijuana_cure, cocaine_cure)
std = (0,0,0,0)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, total, width, yerr=std)
p2 = plt.bar(ind, cure, width,
             bottom=total, yerr=std)

plt.ylabel('Number of people')
plt.title('Perceptions of Risk')
plt.xticks(ind, ('Alcohol', 'Tobacco', 'Marijuana', 'Cocaine'))
plt.legend((p1[0], p2[0]), ('Total','Perceptions of Risk'))

plt.show()
