from shiny import reactive, render
from shiny.express import input, ui
from shinywidgets import render_plotly
import plotly.express as px
import random
from datetime import datetime
from collections import deque

UPDATE_INTERVAL_SECS: int = 1

# Create a deque to store temperature data
temperature_deque = deque(maxlen=20)
latitude_deque = deque(maxlen=20)
longitude_deque = deque(maxlen=20)

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(-18, -16), 1)
    latitude = round(random.uniform(-90, -60), 2)
    longitude = round(random.uniform(-180, 180), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp, "latitude": latitude, "longitude": longitude}
    return latest_dictionary_entry

# Function to update the deque with new temperature data
def update_deque():
    latest_entry = reactive_calc_combined()
    temperature_deque.append(latest_entry['temp'])
    latitude_deque.append(latest_entry['latitude'])
    longitude_deque.append(latest_entry['longitude'])

# Define the Shiny UI Page layout - Page Options
ui.page_opts(title="Antarctic Explorer", fillable=True)

# Display warmer than usual message
ui.p("Warmer than usual", style="color: #ffa500; text-align: center; margin-top: 20px;")

# Define the Shiny UI Page layout - Sidebar
with ui.sidebar(open="open", style="background-color: #333; color: #fff; padding: 20px;"):
    ui.h2("Antarctic Explorer", class_="text-center", style="color: #fff;")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

    # Links section
    ui.h6("Links:", style="color: #fff;")
    ui.a(
        "GitHub Source",
        href="https://github.com/don4ye/cintel-05-cintel/tree/master",
        target="_blank",
        style="color: #fff; text-decoration: none; display: block; margin-bottom: 10px;",
    )
    ui.a(
        "GitHub App",
        href="https://don4ye.github.io/cintel-05-cintel/",
        target="_blank",
        style="color: #fff; text-decoration: none; display: block; margin-bottom: 10px;",
    )
    ui.a(
        "PyShiny",
        href="https://shiny.posit.co/py/",
        target="_blank",
        style="color: #fff; text-decoration: none; display: block; margin-bottom: 10px;",
    )

# Define the Shiny UI Page layout - Main Section
ui.h2("Current Temperature", style="color: #fff; text-align: center; margin-top: 20px;")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} °C"

# Define the Shiny UI Page layout - Live Temperature Map Section
ui.h2("Live Temperature Map", style="color: #fff; text-align: center; margin-top: 20px;")

# Define the Shiny UI Page layout - Temperature History Section
ui.h6("Temperature History", style="font-size: smaller; color: #ccc; text-align: center;")

# Function to render the temperature history
@render.text
def display_temp_history():
    # Update the deque with new data
    update_deque()
    
    # Convert the deque to a list for display
    temp_list = list(temperature_deque)
    
    # Format the temperature history string
    history_str = "\n".join([f"{temp} °C" for temp in temp_list])
    
    return history_str

# Define the Shiny UI Page layout - Plot Section
ui.h6("Temperature Plots", style="font-size: smaller; color: #ccc; text-align: center;")

# Define the Shiny UI Page layout - Main Section
with ui.layout_columns(style="background-color: lightblue; padding: 20px; border: 2px solid blue;"):
    @render_plotly
    def plot1():
        fig = px.line(x=list(range(len(temperature_deque))), y=list(temperature_deque), labels={'x': 'Time', 'y': 'Temperature (°C)'}, title='Temperature over Time')
        fig.update_traces(line=dict(color='#1f77b4', width=2))
        fig.update_layout(title_font_size=20, title_x=0.5, plot_bgcolor='#f0f0f0', margin=dict(l=20, r=20, t=40, b=20))
        return fig

    @render_plotly
    def plot2():
        fig = px.scatter_geo(lat=list(latitude_deque), lon=list(longitude_deque), color=list(temperature_deque),
                             color_continuous_scale='RdBu_r', size=[10]*len(temperature_deque),
                             labels={'color': 'Temperature (°C)'}, title='Live Temperature Map')
        fig.update_geos(projection_type="natural earth")
        fig.update_layout(title_font_size=20, title_x=0.5, plot_bgcolor='#f0f0f0', margin=dict(l=20, r=20, t=40, b=20))
        return fig
