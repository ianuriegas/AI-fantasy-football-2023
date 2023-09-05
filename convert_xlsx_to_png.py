import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel("player_info.xlsx")

# Create a plot of the DataFrame
fig, ax = plt.subplots(figsize=(12, 4)) # Set the size as you like
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

# Make the cells larger to fit the text
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(2.0, 2.0)

# Save the plot as a png file
plt.savefig('player_info.png')
