# **Predicting the Difficulty and Enjoyment Rating of Hiking Trails using Machine Learning**

MyTrails is a backpacking AI that predicts the difficulty and enjoyment rating of hiking trails. To train the machine learning models, a list of ~3000 trails in USA National Parks is used, from AllTrails.com. I include data from trails I have hiked myself as well, and I add a feature to keep track of which trails are mine to help fine-tune the model to my preferences. Another feature is added to keep track the source of the distance and elevation gain data. Elevation gain in particular varies greatly between GPS and topographic sources. A historical weather API (Open-Meteo) is used to collect climate data for each trail. I also use this project to visualize my personal backpacking statistics.

<font size="4">**Data Sources:**</font>
```
- USA National Parks
    - Trails from AllTrails using an API that is now deprecated 
    - N = 3015 (3313 before filters)
    - github.com/j-ane/trail-data/blob/master
    
- Personal Trails
    - Trails logged by me, friends, and family
    - N = ~100
```

<font size="4">**Model Features:**</font>
```
##### MOVEMENT #####
- Distance (km)
- Elevation Gain (m)

##### LOCATION #####
- Country
- Province (or state)
- Region
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
- Number of Reviews (1 for personal trails, often >1 for USA trails)
- Route Source (source of the Distance and Elevation Gain)
- User (person providing the Difficulty and Enjoyment Rating)
```

<font size="4">**Model Targets:**</font>
```
- Difficulty (1-7 scale)
- Enjoyment Rating (1-5 scale)
```

<font size="4">**Summary of Results:**</font>
- Difficulty Model Score: 0.65 to 0.75
- Rating Model Score: 0.2 to 0.3

Trail difficulty can be predicted sufficiently well using a trail's length, elevation gain, climate, location, and physical features. Enjoyment, however, is a different matter. Enjoyment is impacted greatly by trail condition, campsite quality, amount of bugs, hiking companions, weather, and much more that isn't accounted for. It would be better to have more trail ratings linked to individual users, as opposed to the current USA National Park trail ratings that are averaged over many users. This would further help the models adapt to user preferences. If I had a large dataset of individual trail reviews with timestamps and locations, I could use a weather API to collect the specfic weather on each hike.

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
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/WatchlistTrails-PredictionResults.png)