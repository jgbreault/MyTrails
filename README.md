# **Predicting the Difficulty and Enjoyment Rating of Backpacking Trails**

MyTrails is a backpacking AI that predicts the difficulty and enjoyment rating of hiking trails. To train the machine learning models, a list of ~3000 trails in USA National Parks is used, from Alltrails.com. I include data from trails I've hiked myself as well, and I add a feature to keep track of which trails are mine to help fine-tune the model to my preferences. A historical weather API (Open-Meteo) is used to get climate data for each trail. I also use this project to visualize my personal backpacking statistics.

<font size="4">**Summary of Results:**</font>
- Difficulty Model Score: 0.65 to 0.75
- Rating Model Score: 0.2 to 0.3

Trail difficulty can be predicted sufficiently well using a trail's length, elevation gain, climate, location, and physical features. Enjoyment, however, is a different matter. Enjoyment is impacted greatly by trail condition, campsite quality, amount of bugs, hiking companions, weather, and much more that isn't accounted for. It would be better to have a dataset of trail ratings linked to individual users, as opposed to the current USA trail ratings that are averaged over many users. This would further help the models adapt to user preferences. If I had timestamps and locations for each individual review, I could use the weather API to collect the weather on each hike.

<font size="4">**Project Structure:**</font>
```
MyTrails/
├── MyTrails.ipnyb                    # Where I analyse the data and build the models
├── dataSources/
│   ├── AllTrailsUsaNationalParks.csv # USA National Park trails
│   └── MyTrails.csv                  # Data of personal hikes
├── images/                           # Misc generated plots
└── models/                           # Difficulty/Enjoyment models
```

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDataset-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-DistancevsElevationGain(perDay).png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-GroupedbyPark.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-WeatherSummary.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-GroupedbyDayofYear.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-CumulativeDistance.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyBackpackingTrails-PredictionResults.png)