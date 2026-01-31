# **MyTrails: Backpacking AI & Personal Analytics**

MyTrails is a backpacking AI that predicts the difficulty and enjoyment of hiking trails. By combining a dataset of over 3,000 USA National Park trails with data from trails I have hiked myself, machine learning models can be built that are fine-tuned to my preferences. The project uses Scikit-Learn to train models on features like distance, elevation gain, park, and geographical features (caves, waterfalls, etc.). To improve accuracy, I integrated the Open-Meteo API to collect historical weather data for each trail, ensuring the models account for local climate. I also use this project to visualize my personal backpacking statistics and explore trends in my hiking history.

## Key Features

* **Personal Data:** Merged personal hiking data with over 3,000 records from [USA National Parks](https://github.com/j-ane/trail-data/blob/master/alltrails-data.csv). Added a feature to distinguish my records and fine-tune the models to my personal preferences.
* **Climate Data:** Integrated the [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) to enrich the dataset with climate data, improving model performance.
* **Clean Data:** Checked for multicollinearity using VIF. Handled high-cardinality categorical data. Checked for null values.
* **Model Comparisons:** Nine regressors are compared to find the best for difficulty and enjoyment.
* **Feature Selection:** Implemented recursive feature elimination; the feature that improves test MSE most upon removal is iteratively removed until no further removals reduce test MSE.
* **Hyperparameter Tuning:** 5-fold cross-validation is used to tune hyperparameters.
* **Visualization:** Generated detailed visualizations to explore dataset trends and personal statistics.

## Tech Stack

* **Language:** Python
* **Environment:** Jupyter Notebook
* **Machine Learning:** Scikit-Learn
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Plotly
* **API:** Open-Meteo (Historical Weather & Climate Data)
  
## **Summary of Results**

After comparing nine regressors, Gradient Boosting Regressor performed best for predicting difficulty, and Support Vector Regression (SVR) performed best for enjoyment.

- Difficulty Model Score: 0.70 - 0.75
- Enjoyment Model Score: 0.80 - 0.85

## **Plots - Full Dataset**

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDataset-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDatasetTrailCountsbyDifficultyandEnjoyment.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDatasetCorrelationHeatmap.png)

## **Plots - My Trails**

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-GroupedbyPark.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/WeatherSummaryPlot.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-CumulativeDistance.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/TrailDensityByDay.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrailsDayCountsbyMonthandDayofWeek.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrailsCorrelationHeatmap.png)

## **Plots - Prediction Results**

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/TrailsofInterest-PredictedDifficultyvsEnjoyment.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/TrailsofInterest-DistancevsElevationGainwithDifficultyandEnjoymentPredictions.png)

## **Model Targets:**
```
- Difficulty (1-7 scale)
- Enjoyment (1-5 scale)
```

## **Model Features:**
```
##### MOVEMENT #####
- Distance (km)
- Elevation Gain (m)

##### LOCATION #####
- Country
- Province (or state)
- Park

##### PHYSICAL FEATURES #####
- Forest
- Lake
- River
- Waterfall
- Beach
- Historic Site
- Cave
- Hot Spring

##### CLIMATE #####
- Summer Temperature (98th percentile of daily max temps, °C)
- Winter Temperature (2nd percentile of daily min temps, °C)
- Annual Rain (mm)
- Annual Snow (cm)

##### MISCELLANEOUS #####
- Route Type ('loop', 'out and back', or 'point to point')
- Backpacking (whether the trail is known for overnight camping)
- User (person providing the Difficulty and Enjoyment Rating)
```

## Project Structure
```
MyTrails/
├── MyTrails.ipnyb            # Analyse trail data and build the models
├── dataSources/
│   ├── alltrails-climate.csv # Climate data for USA National Park trails
│   ├── alltrails-data.csv    # Other data for USA National Park trails
│   ├── MyTrails.csv          # Data of personal completed hikes
│   └── Shortlist.csv         # Data of personal trails of interest
└── images/                   # Misc generated plots
```