# source https://www.geeksforgeeks.org/introduction-to-dash-in-python/

# importing required libraries 
import dash 
import dash_core_components as dcc	 
import dash_html_components as html 
from dash.dependencies import Input, Output


##########################################################################################################################################################################################
# # 1
# app = dash.Dash() 
# app.layout = html.Div(children =[ 
#     html.H1("Dash Tutorial"), 
#     dcc.Graph( 
#         id ="example", 
#         figure ={ 
#             'data':[ 
#                     {'x':[1, 2, 3, 4, 5], 
#                         'y':[5, 4, 7, 4, 8], 
#                         'type':'line', 
#                         'name':'Trucks'}, 
#                     {'x':[1, 2, 3, 4, 5], 
#                         'y':[6, 3, 5, 3, 7], 
#                         'type':'bar', 
#                         'name':'Ships'} 
#                 ], 
#             'layout':{ 
#                 'title':'Basic Dashboard'
#             } 
#         } 
#     ) 
# ]) 
# if __name__ == '__main__': 
#     app.run_server() 



##########################################################################################################################################################################################
# # 2
# app = dash.Dash() 
# app.layout = html.Div(children =[ 
#     dcc.Input(id ='input', 
#             value ='Enter a number', 
#             type ='text'), 
#     html.Div(id ='output') 
# ]) 

# @app.callback( 
#     Output(component_id ='output', component_property ='children'), 
#     [Input(component_id ='input', component_property ='value')] 
# ) 

# def update_value(input_data): 
#     try: 
#         return str(float(input_data)**2) 
#     except: 
#         return "Error, the input is not a number"

# if __name__ == '__main__': 
#     app.run_server() 



##########################################################################################################################################################################################
# # 3
# app = dash.Dash() 
# app.layout = html.Div(children =[ 
#     dcc.Input(id ='input', 
#             value ='Enter a number', 
#             type ='text'), 
#     html.Div(id ='output') 
# ]) 

# @app.callback( 
#     Output(component_id ='output', component_property ='children'), 
#     [Input(component_id ='input', component_property ='value')] 
# ) 

# def update_value(input_data):
#     global x1, x2, x3, y1, y2, y3
#     x1+=1
#     x2+=1
#     x3+=1
#     y1+=2
#     y2+=2
#     y3+=2
#     try: 
#         import plotly.express as px 
#         fig = px.line(x=[1, 2, 3], y=[1, 2, 3]) # Creating the Figure instance 
#         return fig.to_html()
#     except: 
#         return "Error, the input is not a number"
# x1=y1=1
# x2=y2=2
# x3=y3=3
# if __name__ == '__main__': 
#     app.run_server() 
