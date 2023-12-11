import pandas as pd
import plotly.express as px
import psutil

def cpu_percent():
    N=1
    cpu_usage = psutil.cpu_percent(N) # Calling psutil.cpu_precent() for N seconds
    df = pd.DataFrame({'cpu_usage': [cpu_usage, 100-cpu_usage]})
    fig = px.bar(df, y='cpu_usage', color=['using', 'free'], title='CPU Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
    fig.write_html('first_figure.html', auto_open=True) # showing the plot

def ram_percent():
    ram_usage = psutil.virtual_memory()[2] # Getting % usage of virtual_memory (3rd field)
    df = pd.DataFrame({'ram_usage': [ram_usage, 100-ram_usage]})
    fig = px.bar(df, y='ram_usage', color=['using', 'free'], title='Ram Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
    fig.write_html('first_figure.html', auto_open=True) # showing the plot

def ram_usage():
    total_ram, available_ram, ram_usage_percentage, ram_usage, ram_free = tuple(psutil.virtual_memory())
 
    # pie_chart
    df = pd.DataFrame(
        {
            'items': [ram_usage,ram_free],
            'items_names': ['ram_usage','ram_free']
        })
    fig = px.pie(df, title='Ram Status', values=df['items'], names=df['items_names'], width=500)
    fig.write_html('first_figure.html', auto_open=True)
    
    # # bar_chart
    # df = pd.DataFrame({'ram_usage': [ram_usage, ram_free]})
    # fig = px.bar(df, title='Ram Status', color=['using', 'free'], range_y=[0, total_ram], width=500) # plotting the bar chart 
    # fig.write_html('first_figure.html', auto_open=True)

if __name__ == "__main__":
    # cpu_percent()
    # ram_percent()
    ram_usage()
