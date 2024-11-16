# **Predicting the Difficulty and Enjoyment Rating of Backpacking Trails**

MyTrails is a backpacking AI that predicts the difficulty and enjoyment rating of hiking trails. To train the machine learning models, a list of ~3000 trails in USA National Parks is used, scraped from Alltrails.com. I include data from trails I've hiked myself as well, and I add a feature to keep track of which trails are mine to help fine-tune the model to my preferences. A historical weather API (Open_Meteo) is used to get climate data for each trail. I also use this project to visualize my personal backpacking statistics.

<font size="4">**Summary of Results:**</font>
- Difficulty Model Score: 0.65 to 0.75
- Rating Model Score: 0.2 to 0.3

Trail difficulty can be predicted sufficiently well using a trail's length, elevation gain, climate, location, and physical features. Enjoyment, however, is a different matter. Enjoyment is impacted greatly by trail condition, campsite quality, amount of bugs, and much more that isn't accounted for. It would be better to have a dataset of trail reviews linked to individual users, as opposed to the values I use currently that are averaged over many users. This would be better for building models that can learn user preferences. Also, if I had timestamps and locations for each user review, I could use the weather API to determine the precise weather experienced on each hike.

<font size="4">**Project Structure:**</font>
```
MyTrails/
├── HistoricalWeatherFinder.ipynb # Uses an API to find climate data for base dataset and weather data for my trails
├── MyTrails.ipnyb                # Where I analyse the data and build the models
├── dataSources/
│   ├── AllTrailsUsaNationalParks.csv # Scraped data of all trails in USA National Parks
│   └── MyTrails.csv                  # Data of my personal hikes, and data from friends and family
├── images/ # Misc generated plots
└── models/ # Difficulty and enjoyment rating models used for predictions
```

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDataset-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyPark.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-WeatherSummary.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyDayofYear.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-CumulativeDistance.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/WatchlistTrails-PredictionResults.png)