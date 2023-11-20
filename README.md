# Predicting the Difficulty and Enjoyment Rating of Backpacking Trails

Here, I build machine learning models to predict the difficulty and enjoyment rating of backpacking trails I am personally interested in hiking. The base dataset of ~3000 trails is an exhaustive list of all trails in USA National Parks, scraped from Alltrails.com. I include data from trails I've hiked myself as well. I add a feature to keep track of which trails are mine, helping fine-tune the model to my preferences. A historical weather API is used to get climate data for each trail.

Summary of Steps:

- Get climate data for each trail location using HistoricalWeatherFinder.ipynb
- Convert the elevation gain from AllTrails's GPS data to align with values from topographic data
- Generate statics and visualizations
- Generate difficulty/rating models and predictions
- Visualize and compare prediction results

Summary of Results:

Difficulty Model Score: ~0.70, Rating Model Score: ~0.20

It turns out that a trail's length, elevation gain, climate, and physical features are enough to predict its difficulty with decent accuracy. Enjoyment is a different matter. Enjoyment is impacted greatly by season, weather, preparedness, and who you are hiking with, none of which is accounted for. It would be better to have a dataset of individual trail reviews with timestamps linked to users.

Open images for more plots.

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDataset-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyPark.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-WeatherSummary.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyDayofYear.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-CumulativeDistance.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/WatchlistTrails-PredictionResults.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/GPStoTopographicElevationGain.png)
