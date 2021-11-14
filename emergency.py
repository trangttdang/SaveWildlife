import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from sklearn import linear_model
from matplotlib.cm import ScalarMappable
import shutil

# Return the slope
def give_coef(cases):
    A = np.array([np.arange(len(cases))]).T
    b = np.array([cases]).T

    lr = linear_model.LinearRegression()
    lr.fit(A,b)

    return lr.coef_

# Plot bar chart
def ve(name):
    df = pd.read_csv(name)
    df['Year'] = pd.to_datetime(df['Year'])
    lst = []   
    with open(name) as file:			# Open file
        data = file.read().split("\n")
        data.pop()						# Delete last rows
    header = data[0].split(",")	

    for i in header[1:]:
        lst.append([ i , give_coef(df[i])[0][0] ])

    data_x = header[1:]
    data_y = []
    for i in lst:
        data_y.append(i[1])

    data_color_normalized = [x / max(data_y) for x in data_y]

    fig = plt.figure()	
    fig, ax = plt.subplots()

    my_cmap = plt.cm.get_cmap('YlOrRd')         # color set
    colors = my_cmap(data_color_normalized)    

    ax.bar(data_x, data_y, color=colors )        # plot

    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,max(data_y)))
    sm.set_array([])

    cbar = plt.colorbar(sm)
    cbar.set_label('Level of emergency', rotation=270,labelpad=25)   # Cot mau

    plt.xticks(data_x)
    plt.ylabel("Endangered species increased per year")
    plt.title('Emergency alert')

    file_name = "emergency.jpg"
    fig.savefig(file_name, bbox_inches='tight', dpi=150)
    original = file_name
    target = 'static/images/' + file_name
    shutil.move(original,target)
