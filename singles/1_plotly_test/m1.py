# source https://www.geeksforgeeks.org/python-plotly-tutorial/

# # 1
# import plotly.express as px 
# fig = px.line(x=[1, 2, 3], y=[1, 2, 3]) # Creating the Figure instance 
# print(fig) # printing the figure instance 
# # fig.show() # showing the plot    Which has a bug
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 2
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.line(df, x="species", y="petal_width") # plotting the line chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 3
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.bar(df, x="sepal_width", y="sepal_length") # plotting the bar chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 4
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.histogram(df, x="sepal_length", y="petal_width") # plotting the histogram 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot

# # 5
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.scatter(df, x="species", y="petal_width") # plotting the scatter chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot

# # 6
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.scatter(df, x="species", y="petal_width", size="petal_length", color="species") # plotting the bubble chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot

# # 7
# import plotly.express as px 
# df = px.data.tips() # using the tips dataset 
# fig = px.pie(df, values="total_bill", names="day") # plotting the pie chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot

# # 8
import pandas as pd
import plotly.express as px

def graph(dataframe):
    figure0 = px.pie(dataframe, values=dataframe['POPULATION'], names=dataframe['CONTINENT'], title='Global Population')
    figure0.write_html('first_figure.html', auto_open=True)
    # تست کردم تو فایل نوشت و حدود ۳.۵ مگابایت شده بود. اما کار میکرد.
    # html = figure0.to_html()
    # f = open('t.html', 'w', encoding='utf-8')
    # f.write(html)
    # f.close()
df = pd.DataFrame({'POPULATION':[60, 17, 9, 13, 1], 'CONTINENT':['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']})
graph(df)

# # 9
# import plotly.express as px 
# df = px.data.tips() # data to be plotted 
# fig = px.line_3d(df, x="sex", y="day", z="time", color="sex") # plotting the figure 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot
