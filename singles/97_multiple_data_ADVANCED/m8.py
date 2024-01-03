import pandas as pd
import plotly.express as px
import pymongo
from pymongo.database import Collection

class ComputerInfo():
    def __init__(self, collection:Collection, device_id, cpu_usage=0, ram_usage=0, ram_used=0, ram_free=0, ram_used2=0, ram_free2=0, total_ram=0):
        self.collection = collection
        self.device_id = device_id
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.ram_used = ram_used
        self.ram_free = ram_free
        self.ram_used2 = ram_used2
        self.ram_free2 = ram_free2
        self.total_ram = self.ram_used2+self.ram_free2 # total_ram ro nemidoonestam Alireza Mitoone Befreste ya na be khatere hamin az jame in 2 ta hesab kardam.

    def set_and_get_cpu_percent(self):
        result:dict = self.collection.find_one({"device_id": self.device_id})
        temp:list = result.get('cpu_usage')
        temp.append()
        print(temp)
        for i in result:
            print(i)
        # self.collection.insert_one()
        # self.df = pd.DataFrame({'Amount of CPU usage in %': [self.cpu_usage, 100-self.cpu_usage]})
        # self.fig = px.bar(self.df, y='Amount of CPU usage in %', color=['using', 'free'], title='CPU Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
        # return self.fig.to_html()

    def set_and_get_ram_percent(self):
        self.df = pd.DataFrame({'Amount of RAM usage in %': [self.ram_usage, 100-self.ram_usage]})
        self.fig = px.bar(self.df, y='Amount of RAM usage in %', color=['using', 'free'], title='Ram Usage in %', range_y=[0, 100], width=500) # plotting the bar chart 
        return self.fig.to_html()

    def set_and_get_ram_usage(self):
        # pie_chart
        self.df = pd.DataFrame(
            {
                'items': [self.ram_used, self.ram_free],
                'items_names': ['ram_used','ram_free']
            })
        self.fig = px.pie(self.df, title='Ram Status', values=self.df['items'], names=self.df['items_names'], width=500)
        return self.fig.to_html()
        
    def set_and_get_ram_usage2(self):
        # bar_chart
        self.df = pd.DataFrame({'ram_used': [self.ram_used2, self.ram_free2]})
        self.fig = px.bar(self.df, title='Ram Status', color=['using', 'free'], range_y=[0, self.total_ram], width=500) # plotting the bar chart 
        return self.fig.to_html()
