#Predicting the Difficulty and Enjoyment Rating of Backpacking Trails

Here, I build some machine learning models to predict the difficulty and enjoyment rating of backpacking trails I am personally interested in hiking. Thanks to Jane for the base dataset of ~3000 trails in USA national parks (https://www.kaggle.com/datasets/planejane/national-park-trails).

In addition to this dataset, I include data from trails I've hiked myself. I add a feature to keep track of which trails are mine, which helps fine-tune the model to my preferences. A historical weather API is used to get climate data for each trail.

Open TrailGenie.ipynb for more information.

![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/FullDataset-DistancevsElevationGain.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyPark.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-WeatherSummary.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/MyCompletedTrails-GroupedbyDayofYear.png)
![Image](https://github.com/jgbreault/TrailGenie/blob/main/images/WatchlistTrails-PredictionResults.png)