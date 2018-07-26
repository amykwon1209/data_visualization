import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import drugs

# Some data
list_of_report = drugs.get_reports()

ypain_relievers = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["12-17"]
yalcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"]
ytobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["12-17"]
ymarijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["12-17"]
ycocaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["12-17"]

mpain_relievers = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["18-25"]
malcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["18-25"]
mtobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["18-25"]
mmarijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["18-25"]
mcocaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["18-25"]

opain_relievers = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["26+"]
oalcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["26+"]
otobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["26+"]
omarijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["26+"]
ococaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["26+"]


n_groups = 5
err = (0,0,0,0,0)

old = (opain_relievers, oalcohol, otobacco, omarijuana, ococaine)

young = (ypain_relievers, yalcohol, ytobacco, ymarijuana, ycocaine)

medium = (mpain_relievers, malcohol, mtobacco, mmarijuana, mcocaine)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.7
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, young, bar_width,
                alpha=opacity, color='b',
                yerr=err, error_kw=error_config,
                label='12-17')

rects2 = ax.bar(index + bar_width, medium, bar_width,
                alpha=opacity, color='r',
                yerr=err, error_kw=error_config,
                label='18-25')

rects3 = ax.bar(index + bar_width + bar_width, old, bar_width,
                alpha=opacity, color='g',
                yerr=err, error_kw=error_config,
                label='26+')

ax.set_xlabel('Type of Drugs')
ax.set_ylabel('Number of people')
ax.set_title('Substance abuse among different age groups')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Pain Relievers', 'Alcohol', 'Tobacco', 'Marijuana', 'Cocaine'))
ax.legend()

fig.tight_layout()
plt.show()
