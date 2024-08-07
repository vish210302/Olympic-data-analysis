
# Olympic data analysis -web application
![image](https://github.com/user-attachments/assets/836b965b-1972-4e59-84e0-8327ad538526)

Welcome to the Olympic Data Analysis project! This end-to-end project provides a comprehensive analysis of Olympic data spanning 120 years. It includes detailed Exploratory Data Analysis (EDA), various comparisons, and visualizations. The project is deployed on Render and is designed to offer insights into Olympic Games data.




## Project Description
This project utilizes datasets from Kaggle that include historical data on Olympic athletes and events. It performs thorough EDA and provides various comparisons and visualizations to uncover insights and trends in the Olympic Games.  
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results


## Features
Detailed EDA: Explore trends, patterns, and anomalies in Olympic data.  
Comparative Analysis: Compare performance across different countries, years, and sports.  
Visualizations: Interactive and static charts to illustrate findings.  
## File structure
-idea/: Contains project-specific settings (IDE-related files).   
-__pycache__/: Contains compiled Python files.  
-venv/: Python virtual environment directory.  
-app.py: Main application file to run the analy sis and serve visualizations.  
-athlete_events.csv: Dataset containing athlete events information.  
-helper.py: Helper functions used throughout the project.  
-noc_regions.csv: Dataset containing information on National Olympic Committees (NOCs) and regions.  
-preprocessor.py: Script for data preprocessing and cleaning.  
-requirements.txt: List of required Python packages.
## Installation
To get started with this project, follow these steps:   
1.Clone the repository:  
```python  
git clone https://github.com/vish210302/Olympic-data-analysis.git  
cd Olympic-data-analysis
```  

2.Set Up the Virtual Environment:  
```python 
python -m venv venv
```

3.Activate the Virtual Environment:
On Windows:
```python
venv\Scripts\activate  
```
On macOS/Linux:
```python
source venv/bin/activate
```

4.Install the Required Packages:
```python
pip install -r requirements.txt
```

5.Run the Application:
```python
python app.py
```

Access the deployed application on Render.


## Usage
Once the application is running, you can interact with the visualizations and analyses through the web interface. Explore various sections to view insights and comparisons related to the Olympic data.
