<p align="center">
  <img width="200" height="200" src="https://datagolf.com/static/dg_logo.png">
</p>

# Professional Golfer Strokes Gained Predictor

Goal: predict strokes gained for each Golfer in a field for an upcoming tournament

## Aims of this Project
Using [Data Golf's](https://datagolf.com/) robust API, the goal of this project is to pull 

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
	- this class pulls the current field and relevant golfer details for a given weeks current event.  As of today, 2021-08-27, this is the BMW Championship for the PGA tour.
2. `HistoricalDataGolfExtractor`
	- this class pulls historical round scoring data and betting odds at the time of the event, for each golfer

## Data Processing & Feature Engineering <a class="anchor" id="FE"></a>

## Training<a class="anchor" id="Training"></a>

## Prediction<a class="anchor" id="Prediction"></a>
### Data Processing<a class="anchor" id="predProcessing"></a>
### Output <a class="anchor" id="Output"></a>
Table compairing DraftKing salaries vs predicted total strokes gained

## Future Work






