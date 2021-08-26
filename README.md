<p align="center">
  <img width="200" height="200" src="https://datagolf.com/static/dg_logo.png">
</p>

# Professional Golfer Strokes Gained Predictor

Goal: predict strokes gained for each Golfer in a field for an upcoming tournament

## Aims of this Project
Using [Data Golf's](https://datagolf.com/) robust API, the goal of this project is to predict strokes gained for golfer's participating in an upcoming event.

For now the focus is on men's **PGA** tour, events however, functions have been designed to take other tours that data golf supports ('OPP','EUR', 'KFT') as parameters.

## Strokes Gained: A Primer
[PGA Tour Definition](https://www.pgatour.com/news/2016/05/31/strokes-gained-defined.html)
Strokes gained: total simply compares a player's score to the field average. For example, a player will gain three strokes on the field if he shoots 69 on a day when the field averages 72. A player who shoots 74 on that day loses two strokes to the field.

## Table of Contents 
- [Data Collection](#dataCollection)
- [Data Processing & Feature Engineering](#FE)
- [Training](#Training)
- [Prediction](#Prediction)
	- [Data Processing](predProcessing)
	- [Output](#Output)
## Data Collection <a class="anchor" id="dataCollection"></a>
- The code for the data collection process can by found in the `Extract From Data Golf API.ipynb` jupyter notebook.  It uses two defined classes to pull the data:
1. `CurrentTourneyDataGolfExtractor`
	- this class pulls the current field and relevant golfer details for a given weeks current event, including daily fantasy golf salary information.  This week (2021-08-23), it was for the BMW Championship PGA Tour event.
2. `HistoricalDataGolfExtractor`
	- this class pulls historical round scoring data and betting odds at the time of the event, for each golfer
	- It's important to note that betting odds data on DG is sparse.  Archived odds only go back to mid-2019 and even after that there are 10 events without pre-tournament odds.  For this reason, I only chose to use odds from one book (Bet365).

Once extracted, the two datasets are written as csv files, so that they can be used later for analysis, training, and eventually prediction.

## Data Processing & Feature Engineering <a class="anchor" id="FE"></a>
- The two csv's are read into the notebook `Feature Eng & Training.ipynb` for inspection, analysis, and feature engineering
- Only 78% of rounds have full detailed strokes gained values populated, however total strokes gained `sg_total` is fully populated
- Aggregating the data from rounds to event level

### Feature Engineering
- Creating rolling aggregate features 

### Exploratory Data Analysis

## Training<a class="anchor" id="Training"></a>
### Fitting a Linear Model
- unsuccessfully
### Fitting a Random Forest Model

## Prediction<a class="anchor" id="Prediction"></a>
### Data Processing<a class="anchor" id="predProcessing"></a>
### Output <a class="anchor" id="Output"></a>
Table compairing DraftKing salaries vs predicted total strokes gained

## Future Work






