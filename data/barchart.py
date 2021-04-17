import matplotlib.pyplot as plt

countries = ["USA", "Canada", "Norway", "Russia", "Finland"]
male = [410, 386, 359, 331, 328]
female = [243, 239, 98, 109, 106]

plt.bar(countries, male, 0.4, label="Male" )
plt.bar(countries, female, 0.4, bottom=male, label="female")

plt.xlabel("Countries")
plt.ylabel("Participation")

plt.legend()

plt.show()