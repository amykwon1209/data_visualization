import matplotlib.pyplot as plt
import drugs

# Some data
list_of_report = drugs.get_reports()

pain_relievers = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["12-17"]
alcohol = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"]
tobacco = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["12-17"]
marijuana = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["12-17"]
cocaine = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["12-17"]


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Pain Relievers', 'Alcohol', 'Tobacco', 'Marijuana', 'Cocaine'
sizes = [pain_relievers, alcohol, tobacco, marijuana, cocaine]
explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
