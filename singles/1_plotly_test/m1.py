# source https://www.geeksforgeeks.org/python-plotly-tutorial/

# 1
# نمودار خطی
import plotly.express as px
fig = px.line(x=[1, 2, 3, 4, 5, 6, 7, 8], y=[8, 2, 4, 6, 9, 7, 1, 4]) # Creating the Figure instance
print(fig) # printing the figure instance
# fig.show() # showing the plot    Which has a bug
fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 2
# # نمودار میله ای 
# import plotly.express as px
# import pandas as pd
# df = pd.DataFrame({'POPULATION': [60, 17, 9, 13, 1], 'CONTINENT': ['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']})
# fig = px.bar(df, x="CONTINENT", y="POPULATION") # plotting the bar chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 3
# # نمودار دایره ای
# import plotly.express as px 
# df = px.data.tips() # using the tips dataset. According to the tips dataset documentation, the Tips dataset is a data frame with 244 rows and 7 variables which represents some tipping data where one waiter recorded information about each tip he received over a period of a few months working in one restaurant.
# # print(df.to_string())# total_bill    tip     sex smoker   day    time  size
# fig = px.pie(df, values="total_bill", names="day") # plotting the pie chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # 4
# # نمودار دایره ای
# import pandas as pd
# import plotly.express as px
# def graph(dataframe):
#     figure0 = px.pie(dataframe, values=dataframe['POPULATION'], names=dataframe['CONTINENT'], title='Global Population')
#     figure0.write_html('first_figure.html', auto_open=True)
# df = pd.DataFrame({'POPULATION':[60, 17, 9, 13, 1], 'CONTINENT':['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']})
# graph(df)



















########   اینا دیگه لازم نیست. برای مطالعه شخصی   ########
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset An iris database is a collection of images that contain, at a minimum, the iris region of the eye. The images are typically collected by sensors that operate in the visible spectrum, 380–750 nm, or the near infrared spectrum (NIR), 700–900 nm.
# fig = px.line(df, x="species", y="petal_width") # plotting the line chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # نمودار میله ای 
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset An iris database is a collection of images that contain, at a minimum, the iris region of the eye. The images are typically collected by sensors that operate in the visible spectrum, 380–750 nm, or the near infrared spectrum (NIR), 700–900 nm.
# fig = px.bar(df, x="sepal_width", y="sepal_length") # plotting the bar chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # نمودار میله ای رنگی
# import plotly.express as px
# import pandas as pd
# colors = ['lime', 'cyan', 'blue', 'orange', 'purple']  # Custom colors
# df = pd.DataFrame({'POPULATION': [60, 17, 9, 13, 1], 'CONTINENT': ['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']})
# fig = px.bar(df, x="CONTINENT", y="POPULATION", color="CONTINENT", color_discrete_sequence=colors) # plotting the bar chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # نمودار هیستوگرام
# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.histogram(df, x="sepal_length", y="petal_width") # plotting the histogram 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# import plotly.express as px 
# df = px.data.iris() # using the iris dataset 
# fig = px.scatter(df, x="species", y="petal_width") # plotting the scatter chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# import plotly.express as px
# df = px.data.iris() # using the iris dataset 
# fig = px.scatter(df, x="species", y="petal_width", size="petal_length", color="species") # plotting the bubble chart 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot


# # نمودار دایره ای با رنگ
# import pandas as pd
# import plotly.graph_objects as go
# def graph(dataframe):
#     colors = ['orange', 'cyan', '#333333', 'blue', 'red']
#     figure0 = go.Figure(data=go.Pie(labels=dataframe['CONTINENT'], values=dataframe['POPULATION'], marker=dict(colors=colors)))
#     figure0.update_layout(title='Global Population')
#     figure0.write_html('first_figure.html', auto_open=True)
# df = pd.DataFrame({'POPULATION': [60, 17, 9, 13, 1], 'CONTINENT': ['Asia', 'Africa', 'Europe', 'Americas', 'Oceania']})
# graph(df)


# import plotly.express as px 
# df = px.data.tips() # data to be plotted 
# fig = px.line_3d(df, x="sex", y="day", z="time", color="sex") # plotting the figure 
# fig.write_html('first_figure.html', auto_open=True) # showing the plot
