import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

execucoes = (1, 2)
y_pos = np.arange(len(execucoes))
fitness = [3.06, 12.98]

plt.bar(y_pos, fitness, align='center', alpha=0.3, color="black", width=0.5)
plt.xticks(y_pos, execucoes)
plt.xlabel("""$Configura c \c\~ao$""")
plt.ylabel('Tempo (seg)')
fig.savefig("time.pdf")
plt.show()