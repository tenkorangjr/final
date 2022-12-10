import matplotlib.pyplot as plt
import pandas as pd


def art():
    """Draw environmental art scene graph"""

    df = pd.read_csv(
        'historical-sea-level-for-coastal-ghana-(1993-2015).csv', delimiter=',')

    plt.title("Sea Level Rise in Ghana")
    plt.xlabel("Month")
    plt.ylabel("Sea Level")
    plt.plot(df['Month'], df['Historical Sea Level Anomaly'])


    plt.show()