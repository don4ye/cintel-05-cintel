# cintel-05-cintel
# Antarctic Explorer

## Welcome to the Antarctic Explorer project! This project demonstrates real-time temperature readings in Antarctica through a web dashboard.

## Running the Project Locally

## Initial Start
Clone the Project: Clone this project to your local machine, preferably in your Documents folder.

# git clone <https://github.com/don4ye/cintel-05-cintel.git>

## Set Up Virtual Environment: Open the project folder in VS Code and create a local project virtual environment named .venv. Activate it and install the requirements.

#py -m venv .venv
#.venv\Scripts\Activate
#py -m pip install --upgrade pip setuptools
#py -m pip install --upgrade -r requirements.txt

## Run the Application: Open a terminal in the root project folder and start the application.
#shiny run --reload --launch-browser dashboard/app.py

## Test the App: Open a browser and go to http://127.0.0.1:8000/ to test the application.

# Subsequent Starts
#Activate Virtual Environment: Open a terminal in the root project folder and activate the virtual environment.
#.venv\Scripts\Activate

# Run the Application: Start the application.
#shiny run --reload --launch-browser dashboard/app.py

# Exporting Changes to Docs Folder
#After making changes, export to the docs folder and test GitHub Pages locally.

## Activate Virtual Environment: Open a terminal in the root project folder and activate the virtual environment.
#.venv\Scripts\Activate

#Export to Docs Folder: Remove static assets, export to the docs folder, and start a local server.

#shiny static-assets remove
#shinylive export dashboard docs
#py -m http.server --directory docs --bind localhost 8008

## Test the Pages App: Open a browser and go to http://localhost:8008/ to test the Pages app.

# Pushing Changes to GitHub
## Add, Commit, and Push: After making changes, push them to GitHub.

git add .
git commit -m "Useful commit message"
git push -u origin main

# Enabling GitHub Pages

Before enabling GitHub Pages, ensure that the Pages tab in your repository settings is configured to host from the main branch and the docs folder. After enabling, wait to see the new URL for the hosted app.

This README.md provides detailed instructions on running the project locally, exporting changes to the docs folder, pushing changes to GitHub, and enabling GitHub Pages. Happy exploring the Antarctic Explorer project!