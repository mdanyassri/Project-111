import csv
import pandas as pd
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go 
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#fig = ff.create_distplot([data],["reading_time"], show_hist = False)
#fig.show()

population_mean = statistics.mean(data)
print("mean of population: ", population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, 30):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

stddev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution: ", mean)
print("Standard deviation of sampling distribution: ", stddev)

first_stddev_start, first_stddev_end = mean-stddev, mean+stddev 
second_stddev_start, second_stddev_end = mean-(2*stddev), mean+(2*stddev)
third_stddev_start, third_stddev_end = mean-(3*stddev), mean+(3*stddev)

print("std1", first_stddev_start, first_stddev_end)
print("std2", second_stddev_start, second_stddev_end)
print("std3", third_stddev_start, third_stddev_end)

fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stddev_start, first_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x = [first_stddev_end, first_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stddev_start, second_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x = [second_stddev_end, second_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stddev_start, third_stddev_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x = [third_stddev_end, third_stddev_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

fig = ff.create_distplot([mean_list],["Reading Time"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.show()

z_score = (mean - mean)/stddev
print("The z score is: ", z_score)