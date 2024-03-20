import matplotlib.pyplot as plt

categories = ["Sports","Diet", "Sleep"]
values = [25, 30, 35]

plt.pie(values, labels = categories,autopct = "%1.1f%%", startangle = 90, 
colors =['darkviolet','mediumblue','magenta'] )

plt.title('Category diagram for health support')

plt.show()
