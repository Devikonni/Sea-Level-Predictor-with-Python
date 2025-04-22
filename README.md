# **Sea Level Predictor**

**Project Description**:  
In this project, you will analyze the global average sea level change data from 1880 to predict the sea level rise through the year 2050. The project involves plotting a scatter plot, calculating the line of best fit using linear regression, and predicting future sea levels using the historical data.

---

### **Table of Contents**:
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [License](#license)

---

### **Project Overview**:
- **Objective**: Predict the sea level rise by analyzing historical data from 1880 to 2014 and extending the prediction until 2050.
- **Dataset Source**: The data is sourced from the US Environmental Protection Agency (EPA) and NOAA, detailing the global average sea level change from 1880 to 2014.
- **Key Tasks**:
  - Load the dataset and clean the data.
  - Create a scatter plot to visualize the historical data.
  - Use the `linregress` function from SciPy to create a line of best fit for predictions.
  - Predict the sea level rise in 2050 using two different lines of best fit:
    - A line for all data from 1880 onwards.
    - A line for data from 2000 to the present, predicting sea level rise based on recent trends.

---

### **Technologies Used**:
- Python 3 🐍
- Pandas 📊
- Matplotlib 📉
- SciPy (linregress) 📐
- Git & GitHub 🦸‍♀️

---

### **Features**:
- **Scatter Plot**: Visualize the historical sea level data with year on the x-axis and sea level in inches on the y-axis.
- **Line of Best Fit**: Using SciPy’s `linregress`, create a line of best fit for all data and a line for the data from 2000 onwards.
- **Predictions for 2050**: Extend the line of best fit to predict the sea level rise in 2050.
- **Labels and Titles**: Provide clear titles and labels on the graph for easy understanding.

---

### **Getting Started**:

1. **Clone the repository**:

 
git clone https://github.com/your-username/sea-level-predictor.git

## Install dependencies:

Ensure that you have Python 3 installed. You can install the necessary Python packages by running:

 
pip install pandas matplotlib scipy
## Run the project:

The main script for the project is sea_level_predictor.py. To run the script, use the following command:
 
python sea_level_predictor.py
## Usage:
The project reads a CSV file containing the global average sea level change data from 1880 to 2014. The script creates the following visualizations and predictions:

Scatter Plot: Shows the historical sea level changes from 1880 to 2014.

Line of Best Fit (All Data): A line showing the best fit for the entire dataset from 1880 onward.

Line of Best Fit (Post-2000 Data): A line showing the best fit using data from the year 2000 to the most recent year in the dataset.

Prediction for 2050: The model predicts sea level rise in 2050 for both historical trends and more recent data.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.


