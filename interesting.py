import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2
import drugs

# Some data
list_of_report = drugs.get_reports()

yp = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["12-17"]
ya = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"]
yt = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["12-17"]
ym = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["12-17"]
yc = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["12-17"]

mp = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["18-25"]
ma = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["18-25"]
mt = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["18-25"]
mm = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["18-25"]
mc = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["18-25"]

op = list_of_report[0]["Totals"]["Pain Relievers Abuse Past Year"]["26+"]
oa = list_of_report[0]["Totals"]["Alcohol"]["Abuse Past Year"]["26+"]
ot = list_of_report[0]["Totals"]["Tobacco"]["Use Past Month"]["26+"]
om = list_of_report[0]["Totals"]["Marijuana"]["Used Past Year"]["26+"]
oc = list_of_report[0]["Totals"]["Illicit Drugs"]["Cocaine Used Past Year"]["26+"]

vegetables = ['Pain Relievers', 'Alcohol', 'Tobacco', 'Marijuana', 'Cocaine']
farmers = ['12-17', '18-25', '26+']

harvest = np.array([[yp, mp, op],
                    [ya, ma, oa],
                    [yt, mt, ot],
                    [ym, mm, om],
                    [yc, mc, oc]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Number of people (age 12-17) who used drugs in 2001")
fig.tight_layout()
plt.show()
