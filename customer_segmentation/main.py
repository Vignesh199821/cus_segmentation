
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from customer_segmentation.utils import utils_scripts as ut
import plotly.graph_objs as go
import plotly.io as pio

def get_plots(path):
    df = pd.read_csv(path)
    file_name = []
    #age frequency

    df.drop(["CustomerID"], axis = 1, inplace=True)
    plt.figure(figsize=(10,6))
    plt.title("Ages Frequency")
    sns.axes_style("dark")
    sns.violinplot(y=df["Age"])
    #plt.show()
    plt.savefig(r'temp_files/plt1.png')

    #spending score and annual income

    plt.figure(figsize=(15,6))
    plt.subplot(1,2,1)
    sns.boxplot(y=df["Spending Score (1-100)"], color="red")
    plt.subplot(1,2,2)
    sns.boxplot(y=df["Annual Income (k$)"])
    #plt.show()
    plt.savefig(r'temp_files/plt2.png')

    #distribution of male and female

    genders = df.Gender.value_counts()
    sns.set_style("darkgrid")
    plt.figure(figsize=(10,4))
    sns.barplot(x=genders.index, y=genders.values)
    #plt.show()
    file_name = ut.random_word(6)
    plt.savefig(r'temp_files/plt3.png')


    #no of customers in each age group

    age18_25 = df.Age[(df.Age <= 25) & (df.Age >= 18)]
    age26_35 = df.Age[(df.Age <= 35) & (df.Age >= 26)]
    age36_45 = df.Age[(df.Age <= 45) & (df.Age >= 36)]
    age46_55 = df.Age[(df.Age <= 55) & (df.Age >= 46)]
    age55above = df.Age[df.Age >= 56]
    x = ["18-25","26-35","36-45","46-55","55+"]
    y = [len(age18_25.values),len(age26_35.values),len(age36_45.values),len(age46_55.values),len(age55above.values)]
    plt.figure(figsize=(15,6))
    sns.barplot(x=x, y=y, palette="rocket")
    plt.title("Number of Customer and Ages")
    plt.xlabel("Age")
    plt.ylabel("Number of Customer")
    #plt.show()
    plt.savefig(r'temp_files/plt4.png')
    #no of customers according to the spending score

    ss1_20 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 1) & (df["Spending Score (1-100)"] <= 20)]
    ss21_40 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 21) & (df["Spending Score (1-100)"] <= 40)]
    ss41_60 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 41) & (df["Spending Score (1-100)"] <= 60)]
    ss61_80 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 61) & (df["Spending Score (1-100)"] <= 80)]
    ss81_100 = df["Spending Score (1-100)"][(df["Spending Score (1-100)"] >= 81) & (df["Spending Score (1-100)"] <= 100)]

    ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]
    ssy = [len(ss1_20.values), len(ss21_40.values), len(ss41_60.values), len(ss61_80.values), len(ss81_100.values)]

    plt.figure(figsize=(15,6))
    sns.barplot(x=ssx, y=ssy, palette="nipy_spectral_r")
    plt.title("Spending Scores")
    plt.xlabel("Score")
    plt.ylabel("Number of Customer Having the Score")
    #plt.show()
    plt.savefig(r'temp_files/plt5.png')

    #no of customers according to annual income

    ai0_30 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 0) & (df["Annual Income (k$)"] <= 30)]
    ai31_60 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 31) & (df["Annual Income (k$)"] <= 60)]
    ai61_90 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 61) & (df["Annual Income (k$)"] <= 90)]
    ai91_120 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 91) & (df["Annual Income (k$)"] <= 120)]
    ai121_150 = df["Annual Income (k$)"][(df["Annual Income (k$)"] >= 121) & (df["Annual Income (k$)"] <= 150)]

    aix = ["$ 0 - 30,000", "$ 30,001 - 60,000", "$ 60,001 - 90,000", "$ 90,001 - 120,000", "$ 120,001 - 150,000"]
    aiy = [len(ai0_30.values), len(ai31_60.values), len(ai61_90.values), len(ai91_120.values), len(ai121_150.values)]

    plt.figure(figsize=(15,6))
    sns.barplot(x=aix, y=aiy, palette="Set2")
    plt.title("Annual Incomes")
    plt.xlabel("Income")
    plt.ylabel("Number of Customer")
    #plt.show()
    plt.savefig(r'temp_files/plt6.png')


    #wcss

    wcss = []
    for k in range(1,11):
        kmeans = KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(df.iloc[:,1:])
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(12,6))
    plt.grid()
    plt.plot(range(1,11),wcss, linewidth=2, color="red", marker ="8")
    plt.xlabel("K Value")
    plt.xticks(np.arange(1,11,1))
    plt.ylabel("WCSS")
    #plt.show()
    file_name = ut.random_word(6)
    plt.savefig(r'temp_files/plt7.png')


    #spending score vs annnual icome  and age 3D plot

    km = KMeans(n_clusters=5)
    clusters = km.fit_predict(df.iloc[:,1:])
    df["label"] = clusters


    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df.Age[df.label == 0], df["Annual Income (k$)"][df.label == 0], df["Spending Score (1-100)"][df.label == 0], c='blue', s=60)
    ax.scatter(df.Age[df.label == 1], df["Annual Income (k$)"][df.label == 1], df["Spending Score (1-100)"][df.label == 1], c='red', s=60)
    ax.scatter(df.Age[df.label == 2], df["Annual Income (k$)"][df.label == 2], df["Spending Score (1-100)"][df.label == 2], c='green', s=60)
    ax.scatter(df.Age[df.label == 3], df["Annual Income (k$)"][df.label == 3], df["Spending Score (1-100)"][df.label == 3], c='orange', s=60)
    ax.scatter(df.Age[df.label == 4], df["Annual Income (k$)"][df.label == 4], df["Spending Score (1-100)"][df.label == 4], c='purple', s=60)
    ax.view_init(30, 185)
    plt.xlabel("Age")
    plt.ylabel("Annual Income (k$)")
    ax.set_zlabel('Spending Score (1-100)')
    #plt.show()
    #file_name = ut.random_word(6)
    #plt.savefig(file_name+'.png')




    km = KMeans(n_clusters=5)
    clusters = km.fit_predict(df.iloc[:,1:])
    df["label"] = clusters

    # create 3D scatter plot using plotly
    fig = go.Figure(data=[go.Scatter3d(
        y=df["Age"],
        x=df["Annual Income (k$)"],
        z=df["Spending Score (1-100)"],
        mode="markers",
        marker=dict(
            color=clusters,
            size=6,
            opacity=0.8
        )
    )])
    fig.update_layout(scene=dict(xaxis_title='Age', yaxis_title='Annual Income (k$)', zaxis_title='Spending Score (1-100)'))
    # save the plot as an interactive HTML file
    save_path = '/'.join(('temp_files','3d_plot.html'))
    pio.write_html(fig, file=save_path, auto_open=False)


    # pass the HTML file to frontend

    with open(save_path, 'r', encoding='utf-8') as file:
        html_string = file.read()
      #  print(html_string)
    # now you can pass the html_string to your frontend to display the plot
    return 'done'

