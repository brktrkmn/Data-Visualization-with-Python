#gold medals total = 315
#silver medals total = 203
#bronze medals total = 107

import matplotlib.pyplot as plt

values = [315, 230, 107]
labels = ["Gold medals (315)", "Silver medals (203)", "Bronze Medals (107)"]
colors = ['#D6AF36', '#D7D7D7', '#824A02']

plt.title('Medals won by Canada', fontdict={'fontsize':15,'fontweight':'bold'})

plt.pie(values, labels=labels, colors=colors)
plt.show()