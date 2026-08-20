import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

goal = 1_000_000
mmf_rate = 0.11 / 12
monthly_amounts = [5000, 10000, 20000, 40000, 80000, 100000, 200000, 500000]

months_saving = goal / np.array(monthly_amounts)
months_investing = np.log(1 + goal * mmf_rate / np.array(monthly_amounts)) / np.log(1 + mmf_rate)
time_saved = months_saving - months_investing

plt.figure(figsize=(10,6))
plt.plot(monthly_amounts, months_saving, label='Saving', marker='o')
plt.plot(monthly_amounts, months_investing, label='MMF 11%', marker='o')
plt.xlabel('Monthly Contribution (Ksh)')
plt.ylabel('Months to Ksh 1M')
plt.title('Saving vs Investing: The Gap Closes')
plt.legend()
plt.grid(True)
plt.savefig('chart1_line.png')
