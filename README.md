# quasar_project

Paulina Volkova's QUASAR project

How to run: 
1) Download the zip folder and extract files to a location of your choosing. Navigate in the terminal to where you saved the file: cd path/to/quasar_project-main
2) The script requires python, pandas, and plotly to run.
   1) If not installed, install python: https://realpython.com/installing-python/
   2) If not installed, install pandas: pip install pandas
   3) If not installed, install plotly: pip install plotly
3) Run the python file: python ./plotting_script.py

Design choices: 
1) ECG vs EEG scaling: because Plotly automatically scales the data according to its y-axis, the easiest method I found to scale the data was to create two y-axes.
2) Dropdown menu: Given the amount of data, I felt that creating a channel dropdown menu would be the most readable option. For that, I referenced various resources:
   1) Plotly Community Forum: https://community.plotly.com/t/plotly-express-dropdown-menu-between-2-dataframes/82304
   2) Stack Overflow (accessed from Plotly Community Forum): https://stackoverflow.com/questions/59070876/plotly-how-do-the-buttons-for-the-update-menus-really-work
   3) ChatGPT (help to resolve issues of disappearance of titles between menus and inconsistent visibility of traces)
4) CM distinction: I made CM channel trace to be a dotted graph to indicate its distinction from other ECG traces

Future Work: 
1) I wanted to make it possible to convert between milli and microvolts, but I couldn't figure out an efficient enough method to do that in the given time. In the future, I would want to implement that feature.
2) To improve readability, my next step in addition to the channel dropdown menu would be to implement subplots. In other words, whenever a menu is changed (for instance, between ECG channels to EEG channels), I would separate all the channels into different subplots instead of having a single plot with all the data. This is especially critical for EEG where there are many channels.

 
