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




x = np.linspace(0, 2 * np.pi, 500)
y = 2 * np.sin(x)

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)

ax0.plot(x, y)
ax0.set_title('Number of people')

ax1.plot(x, y)
ax1.set_title('Number of people')



# Hide the right and top spines
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

ax2.plot(x, y)
ax2.set_title('Number of people')

# Only draw spine between the y-ticks
ax2.spines['left'].set_bounds(-1, 1)
# Hide the right and top spines
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

# Tweak spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=0.5)
plt.show()
