import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 32}

plt.rc('font', **font)

fig, ax = plt.subplots()

plt.xlabel('Number of Pedestrians', weight='bold', fontsize=40)
plt.ylabel('Close Contacts', weight='bold', fontsize=40)

x =[0, 1, 2]
nums = ['100', '150', '200']
avgs = [243, 527, 871]
plt.ylim([0, 1000])

plt.xticks(x,nums)
plt.plot(nums, avgs, marker='o', color="maroon", linewidth=4)

plt.errorbar([0], [243], yerr=[[186], [130]], capsize=6, elinewidth=1,  ecolor='lightcoral')
plt.errorbar([1], [527], yerr=[[377], [278]], capsize=6, elinewidth=1, ecolor='lightcoral')
plt.errorbar([2], [871], yerr=[[614], [456]], capsize=6, elinewidth=1, ecolor='lightcoral')

plt.axhline(y=247, xmin=0.05, xmax=0.5, color="indianred", linestyle='dashed')
plt.axvline(x=1, ymin=0.243, ymax=0.527, color="indianred", linestyle='dashed')

plt.axhline(y=527, xmin=0.5, xmax=0.95, color="indianred", linestyle='dashed')
plt.axvline(x=2, ymin=0.527, ymax=0.871, color="indianred", linestyle='dashed')

plt.text(1.02, 365, 'Δ 130%', fontsize=32)
plt.text(1.75, 640, 'Δ 70%', fontsize=32)

plt.show()

