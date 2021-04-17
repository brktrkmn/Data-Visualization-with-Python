import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14,10))

names = ["USA", "Canada", "Norway", "Russia", "Finland"]
male = [410, 386, 359, 331, 328]
female = [243, 239, 98, 109, 106]
positions = [0, 1, 2, 3]
positions2 = [0.3, 1.3, 2.3, 3.3]
positions3 = [0.15, 1.15, 2.15, 3.15]

plt.bar(positions, male, width=0.3,)
plt.bar(positions2, female, width=0.3)
plt.xticks(positions3, names)
#plt.xlabel('Year')
#plt.ylabel('Female athletes')
#plt.title('Female athletes participation in every Olympics', fontdict={'fontsize':13,'fontweight':'bold'})

#plt.axis( [1920, 2020, 0, 300])

plt.show()