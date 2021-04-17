# import matplotlib.pyplot as plt

# medals = [42, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 74, 40, 42, 49, 75, 68, 91, 90] 
# years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1560, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]


# plt.plot(medals, years, color= '#E63828', linewidth= 1.0)

# plt.xlabel("Medals won total")
# plt.ylabel("Year")

# plt.title("Medals won in each Winter Olympics")

# plt.show()


#from matplotlib import pyplot as plt
#from matplotlib import dates as mpl_dates
#import pandas as pd
#from datetime import datetime, timedelta

#plt.style.use('seaborn')


#dates =[
#	datetime(1924, 1, 1),
#	datetime(1928, 1, 1), 
#	datetime(1932, 1, 1),
#	datetime(1936, 1, 1),
#	datetime(1948, 1, 1),
#	datetime(1952, 1, 1),
#	datetime(1956, 1, 1),
#	datetime(1960, 1, 1),
#	datetime(1964, 1, 1),
#	datetime(1968, 1, 1),
#	datetime(1972, 1, 1),
#	datetime(1976, 1, 1),
#	datetime(1980, 1, 1),
#	datetime(1984, 1, 1),
#	datetime(1988, 1, 1),
#	datetime(1992, 1, 1),
#	datetime(1994, 1, 1),
#	datetime(1998, 1, 1),
#	datetime(2002, 1, 1),
#	datetime(2006, 1, 1),
#	datetime(2010, 1, 1),
#	datetime(2014, 1, 1)
#]

#y = [42, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 74, 40, 42, 49, 75, 68, 91, 90]

#plt.plot_date(datetime, y, linestyle='solid')

#date_format = mpl_dates.DateFormatter('%b, %d %Y')



#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd

#year = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1560, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
#medals = [42, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 74, 40, 42, 49, 75, 68, 91, 90]

#plt.plot(medals, year)

#plt.title('Medals won total in each Olympics', fontdict={'fontsize':15,'fontweight':'bold'})
#plt.xlabel('Year')
#plt.ylabel('Medals')

#plt.xticks([1924, 1928, 1932, 1936, 1948, 1952, 1956, 1560, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014])
#plt.yticks([42, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 74, 40, 42, 49, 75, 68, 91, 90])

#plt.show()

import matplotlib.pyplot as plt

year = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1560, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
medals = [42, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 74, 40, 42, 49, 75, 68, 91, 90]

plt.plot(year, medals, 'ok', color= '#E63828')
plt.xlabel('Year')
plt.ylabel('Medals won')
plt.title('Medals won by Canada in every Olympics', fontdict={'fontsize':15,'fontweight':'bold'})

plt.axis( [1920, 2020, 0, 100])

plt.show()