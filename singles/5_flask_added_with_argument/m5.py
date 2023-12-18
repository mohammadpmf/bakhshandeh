import pandas as pd
import plotly.express as px

def cpu_percent(cpu_usage):
    cpu_usage = float(cpu_usage)
    df = pd.DataFrame({'cpu_usage': [cpu_usage, 100-cpu_usage]})
    fig = px.bar(df, y='cpu_usage', color=['using', 'free'], title='CPU Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
    return fig.to_html()

def ram_percent(ram_usage):
    ram_usage = float(ram_usage)
    df = pd.DataFrame({'ram_usage': [ram_usage, 100-ram_usage]})
    fig = px.bar(df, y='ram_usage', color=['using', 'free'], title='Ram Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
    return fig.to_html()

def get_ram_usage(ram_used, ram_free):
    ram_used = float(ram_used)
    ram_free = float(ram_free)
    # pie_chart
    df = pd.DataFrame(
        {
            'items': [ram_used,ram_free],
            'items_names': ['ram_used','ram_free']
        })
    fig = px.pie(df, title='Ram Status', values=df['items'], names=df['items_names'], width=500)
    return fig.to_html()
    
def get_ram_usage2(ram_used, ram_free, total_ram):
    ram_used = float(ram_used)
    ram_free = float(ram_free)
    total_ram = float(total_ram)
    # bar_chart
    df = pd.DataFrame({'ram_used': [ram_used, ram_free]})
    fig = px.bar(df, title='Ram Status', color=['using', 'free'], range_y=[0, total_ram], width=500) # plotting the bar chart 
    return fig.to_html()

if __name__ == "__main__":
    # cpu_percent()
    # ram_percent()
    get_ram_usage()
