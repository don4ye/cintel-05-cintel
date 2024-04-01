from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from faicons import icon_svg


UPDATE_INTERVAL_SECS: int = 1

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)
    temp = round(random.uniform(-18, -16), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}
    return latest_dictionary_entry

# Define the Shiny UI Page layout - Page Options
ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# Define the Shiny UI Page layout - Sidebar
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

# Define the Shiny UI Page layout - Main Section
ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("warmer than usual")

# Assuming icon_svg is imported from faicons
icon_svg("sun")
icon_svg("moon") 
icon_svg("star")
icon_svg("mars")

ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"
