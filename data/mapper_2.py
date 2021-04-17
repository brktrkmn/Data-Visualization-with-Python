import matplotlib.pyplot as plt

year = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1560, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
women = [6, 6, 6, 9, 15, 18, 27, 39, 46, 46, 45, 51, 51, 54, 63, 99, 111, 189, 208, 232, 233, 272]

plt.plot(year, women, 'ok', color= '#E63828')
plt.xlabel('Year')
plt.ylabel('Female athletes')
plt.title('Female athletes participation in every Olympics', fontdict={'fontsize':13,'fontweight':'bold'})

plt.axis( [1920, 2020, 0, 300])

plt.show()