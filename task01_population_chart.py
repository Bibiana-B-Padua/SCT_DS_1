import matplotlib.pyplot as plt

age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population_millions = [512, 807, 98]  # In millions
percentages = [36.1, 57.0, 6.9]
colors = ['gold', 'deepskyblue', 'hotpink']

plt.figure(figsize=(8, 6))
bars = plt.bar(age_groups, population_millions, color=colors)

for i, (bar, pct) in enumerate(zip(bars, percentages)):
    plt.text(bar.get_x() + bar.get_width() / 2, 
             bar.get_height() + 10, 
             f'{pct}%', 
             ha='center', 
             va='bottom', 
             fontsize=12, 
             fontweight='bold')

plt.title("India's Population Distribution by Age (2022)", fontsize=14, fontweight='bold')
plt.xlabel("Age Groups")
plt.ylabel("Population (in Millions)")
plt.ylim(0, 900)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
