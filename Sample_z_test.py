import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("C110.csv")
data = df["average"].tolist()
population_mean = statistics.mean(data)
sd = statistics.stdev(data)

def random_mean_finding(counter):
    data_set = []
    for i in range(0,counter):
        sample_list = random.randint(0,len(data)-1)
        value = data[sample_list]
        data_set.append(value)
    Mean = statistics.mean(data_set)
    return Mean

def create_figure(Mean_list):
    df = Mean_list
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_mean_finding(372)
        mean_list.append(set_of_means)
        
    sample_mean_for_ZTest = set_of_means
    ZScore = sample_mean_for_ZTest*population_mean/sd
    create_figure(mean_list)
    mean_100 = statistics.mean(mean_list)
    print("\nMean of sampling distribution:", mean_100)
    print("\nSample's mean list:", mean_list)
    print("\nZ score is:", ZScore)
setup()