import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

# Read CSV into pandas
# data = pd.read_csv(r"cars.csv")
# data.head()
# df = pd.DataFrame(data)

results = {
    "c-hiredis": [944000], "cristal-redis": [2315000],
    "go-radix": [900000], "go-redigo": [2310000],
    "java-jedis": [387000], "node-ioredis": [100000], "node-redis": [110000],
    "python-aredis": [147000], "ruby-hiredis": [60000], "ruby-redis": [200000]
}
df = pd.DataFrame.from_dict(data=results)

name = list(df.columns)
price = df.values.tolist()[0]

# Figure Size
fig, ax = plt.subplots(figsize=(16, 9))

# define a list of colors to use for the bars
colors = ['green', 'blue', 'red', 'orange', 'purple']

# Horizontal Bar Plot
ax.barh(name, price, color=colors)

# create a formatter to format the tick labels as integers
formatter = ticker.ScalarFormatter(useOffset=False)
formatter.set_scientific(False)

# create a locator to adjust the tick positions to the nearest integer
locator = ticker.MaxNLocator(integer=True)

# apply the formatter and locator to the x-axis of the first subplot
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_major_locator(locator)

# # Horizontal Bar Plot
# plt.bar(name[0:10], price[0:10])
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad=5)
ax.yaxis.set_tick_params(pad=10)

# Add x, y gridlines
ax.grid(visible=True, color='grey',
        linestyle='-.', linewidth=1,
        alpha=0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width() + 0, i.get_y() + 0.5,
             str(round((i.get_width()), 2)),
             fontsize=10, fontweight='bold',
             color='grey')

# Add Plot Title
ax.set_title('Programming langs and his redis modules performance',
             loc='left', )

# set the x-axis label for the first subplot
ax.set_xlabel('Set command per second')

# Add Text watermark
fig.text(0.9, 0.15, 'Improve predictions-home', fontsize=12,
         color='grey', ha='right', va='bottom',
         alpha=0.7)

# Show Plot
plt.show()
