#medals won by Canada = 625
#medals won by the other countries = 5145

import matplotlib.pyplot as plt

values = [625, 5145]
labels = ["Canada - 625 medals", "Other Countries - 5145 medals"]
colors = ['#E63828', 'lightskyblue']
explode = (0, 0.05)
plt.title('Total Medals Comparison', fontdict={'fontsize':15,'fontweight':'bold'})

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()
