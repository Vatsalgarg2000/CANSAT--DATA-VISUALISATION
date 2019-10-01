import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')
plt.title('Live Plot')
plt.xlabel('Time')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['first_column']
    y2 = data['second_column']
    y3 = data['third_column']
    y4 = data['fourth_column']
    y5 = data['fifth_column']
    y6 = data['sixth_column']
    y7 = data['seventh_column']
    y8 = data['eight_column']
    
    plt.cla()

    plt.plot(x, y1, label='Plot 1',color= 'b')
    plt.plot(x, y2, label='Plot 2',color= 'c')
    plt.plot(x ,y3 ,label='Plot 3',color= 'k')
    plt.plot(x, y4, label='Plot 4',color= 'r')
    plt.plot(x, y5, label='Plot 5',color= 'm')
    plt.plot(x ,y6 ,label='Plot 6',color= 'y')
    plt.plot(x, y7, label='Plot 7',color= 'g')
    plt.plot(x, y8, label='Plot 8',color= 'w')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()