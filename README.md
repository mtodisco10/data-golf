<p align="center">
  <img width="200" height="200" src="https://datagolf.com/static/dg_logo.png">
</p>

# Pro Golfer Strokes Gained Predictor

## Aims of the Project
Using [Data Golf's](https://datagolf.com/) robust API, the goal of this project is to extract historical round scoring data and build a model to accurately predict the **total strokes gained** for golfers participating in an upcoming event. 

Comparing prediction outputs with daily fantasy salaries will be used to help inform betting strategies and optimize lineup construction.

Notes:
- For now the focus is on men's **PGA** tour, events however, functions have been designed to take other tours that data golf supports (European, Korn Ferry, etc.) as arguements.
- The model is trained to predict on the event level (ie over 4 collective rounds), however individual round prediction is planned for future work.

## Strokes Gained: A Primer
Strokes gained: simply compares a player's score to the field average. For example, a player will gain three strokes on the field if he shoots 69 on a day when the field averages 72. A player who shoots 74 on that day loses two strokes to the field.

For more details see the [PGA Tour Definition](https://www.pgatour.com/news/2016/05/31/strokes-gained-defined.html).

For this iteration of the project, only Total Strokes Gained is incorporated, however, more granular strokes gained metrics such as strokes gained putting, tee to green, around the green, etc. will be included in future iterations.

## Table of Contents 
- [Data Collection](#dataCollection)
- [Data Processing](#DP)
	- [Feature Engineering](#FE)
	- [Exploratory Analysis](#EA)
- [Training](#Training)
	- [Linear Regression](#LR)
	- [Random Forest](#RF)
- [Prediction](#Prediction)
	- [Data Processing](predProcessing)
	- [Output](#Output)
- [Future Work](#FW)
## Data Collection <a class="anchor" id="dataCollection"></a>
- The code for the data collection process can by found in the `Extract From Data Golf API.ipynb` jupyter notebook.  It uses two defined classes to pull the data:
1. `CurrentTourneyDataGolfExtractor`
	- This class pulls the current field and relevant golfer details for a given weeks current event, including daily fantasy golf salary information.  This week's (2021-08-23) tournament was the **BMW Championship** at Caves Valley Golf Club in Maryland.
2. `HistoricalDataGolfExtractor`
	- This class pulls historical round scoring data and betting odds at the time of the event, for each golfer
	- It's important to note that betting odds data on DG is sparse.  Archived odds only go back to mid-2019 and even after that there are 10 events without pre-tournament odds.  For this reason, I only chose to use odds from one book (Bet365).

Once extracted, the two datasets are written as csv files, so that they can be used later for analysis, training, and eventually prediction.

## Data Processing <a class="anchor" id="DP"></a>
- The two csv's are read into the notebook `Feature Eng & Training.ipynb` for inspection, analysis, and feature engineering
- Only 72% of events have full detailed strokes gained values populated, however total strokes gained `sg_total` is fully populated, which is our target variable.
- The historical data is presented on the round by round level, so it was necessary to `groupby` event fields and aggregate numeric fields for each round either by it's average or sum.

### Feature Engineering <a class="anchor" id="FE"></a>
- The most difficult part of creating usable features, was that they needed to be lagging indicators.  For example, how many times did a golfer finish in the top 10 in his last 5 events **prior** to the current event?
- In order to handle that I made a function `create_rolling_agg_features_by_golfer`, which for a given field and period calculates the lagging aggregates so that they can be used for modeling.
	- The function is located in the [utils.py](https://github.com/mtodisco10/data-golf/blob/master/notebooks/utils.py) file.

## Training<a class="anchor" id="Training"></a>
### Fitting a Linear Model<a class="anchor" id="LR"></a>
A statsmodels OLS model was initially fit on the dataset with an R^2 value of .15.  

However, several linear regression assumptions were violated, namely non-linearity.

<p align="center">
  <img width="500" height="500" src="/images/linearity_check.png">
</p>

So I moved on to a less stringent model
### Fitting a Random Forest Model<a class="anchor" id="RF"></a>
A Random Forest model performed slightly bette with an R^2 value of .17 on test data.

The odds prior to a tournment starting was by far the most important feature.

<p align="center">
  <img width="600" height="400" src="/images/feat_imp.png">
</p>

## Prediction<a class="anchor" id="Prediction"></a>
### Data preprocessing<a class="anchor" id="predProcessing"></a>
Data from the pre-tourney file is appended to the historical event data.
Engineered features along with the lag features are calculated just as they are before training.
The current event data is then subsetted to be used for prediction.

### Output <a class="anchor" id="Output"></a>
Predictions are made on the new data using the RandomForest model.

Table compairing DraftKing salaries vs predicted total strokes gained

**Top 5 Golfers with Positive rnk_diff**
<p align="center">
  <img width="700" height="250" src="/images/top_10_rnk_diff.png">
</p>

**Bottom 5 Golfers with Negative rnk_diff**
<p align="center">
  <img width="700" height="250" src="/images/bottom_10_rnk_diff.png">
</p>

## Future Work<a class="anchor" id="FW"></a>
- Performing transformations to appease linear regression assumptions
- Continued feature engineering
	- Previous course/event performance
	- Course type performance: long vs short, links style, green types, etc.
- Data collection from additional data sources such as [Fantasy National](https://www.fantasynational.com/)
	- full strokes gained data (T2G, APP, PUTT)
- Round by Round predictions for "Showdown" daily fantasy golf





