# **Predicting the Difficulty and Enjoyment of Hiking Trails using Machine Learning**

MyTrails is a backpacking AI that predicts the difficulty and enjoyment rating of hiking trails. A list of over 3000 trails from USA National Parks is used to train the machine learning models, from AllTrails. I also include data from trails I have hiked myself, and I add a feature to distinguish them, to help fine-tune the models to my preferences. Other features include distance, elevation gain, park, seen geographical features, and much more. A historical weather API ([https://open-meteo.com/en/docs/historical-weather-api](Open-Meteo)) is used to collect climate data for each trail. I also use this project to visualize my personal backpacking statistics.

<font size="4">**Summary of Results:**</font>
- Difficulty Model Score: 0.70 - 0.75
- Rating Model Score: 0.80 - 0.85

<font size="4">**Data Sources:**</font>
```
- USA National Parks
    - Trails from AllTrails using an API that is now deprecated 
    - N = 3313
    - github.com/j-ane/trail-data/blob/master
    
- Personal Trails
    - Trails logged by me, friends, and family
    - N < 100
```

<font size="4">**Model Targets:**</font>
```
- Difficulty (1-7 scale)
- Enjoyment Rating (1-5 scale)
```

<font size="4">**Model Features:**</font>
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

<font size="4">**Project Structure:**</font>
```
MyTrails/
├── MyTrails.ipnyb            # Analyse trail data and build the models
├── dataSources/
│   ├── alltrails-climate.csv # Climate data for USA National Park trails
│   ├── alltrails-data.csv    # Other data for USA National Park trails
│   └── MyTrails.csv          # Data of personal completed hikes
│   └── Shortlist.csv         # Data of personal trails of interest
└── images/                   # Misc generated plots
```

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
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/TrailsofInterest-PredictedDifficultyvsEnjoymentwithDifficultyandEnjoymentPredictions.png)

