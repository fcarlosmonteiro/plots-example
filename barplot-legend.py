import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

fig, ax = plt.subplots()

execucoes = ('boolop',
'calendar',
'changerMoney',
'coordinates',
'grades',
'orelse',
'triangle',
'typeTriangle'
)
y_pos = np.arange(len(execucoes))
tool = [0.88,
        0.95,
        0.84,
        0.75,
        0.71,
        1.00,
        0.83,
        0.90
        ]
random = [0.62,
          0.74,
          0.57,
          0.56,
          0.61,
          0.68,
          0.67,
          0.77
          ]

plt.bar(y_pos, tool, align='center', alpha=0.8, color="black", width=0.2, label='Tool')
plt.bar(y_pos+0.2, random, align='center', alpha=0.8, color="red", width=0.2, label='Random Generation')
plt.xticks(y_pos, execucoes, fontsize=11)
plt.legend(loc="upper right")
plt.xlabel('Programs')
plt.ylabel('Mutation Score')
fig.savefig("time.pdf")
plt.show()
