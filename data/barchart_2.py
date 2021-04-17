import matplotlib.pyplot as plt

branches = ["Skiing", "Ice Hockey", "Scating", "Bobsleigh", "Biathlon"]
male = [1130, 1231, 665, 416, 270 ]
female = [651, 305, 564, 36, 150]

plt.bar(branches, male, 0.4, label="Male" )
plt.bar(branches, female, 0.4, bottom=male, label="female")

plt.xlabel("Branches")
plt.ylabel("Participation")

plt.legend()

plt.show()