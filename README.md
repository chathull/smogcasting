# SmogCasting

**Author: C. Hull** (github: [chat.hull](http://github.com/chathull); personal website: [chathull.com](http://www.chathull.com))

## App

The final product, an AQI forecaster for Santiago, Chile, can be seen at [smogcasting.herokuapp.com](https://smogcasting.herokuapp.com/).

## Introduction 

Here I analyze and model historical data of the air quality index (AQI) in Santiago, Chile in order to produce an AQI forecast for Santiago residents.  The primary tool I use to model the data and produce the forecast is the Facebook Prophet time-series forecasting software (https://facebook.github.io/prophet).  Prophet is a type of additive regression model that calculates annual, weekly, and daily seasonality trends along with a drift term.

The data for a representative weather station in central Santiago can be found here: https://sinca.mma.gob.cl/index.php/estacion/index/key/D14

Shout-outs to the many posts/github pages that helped me out!

* Laura Fedoruk: time-series manipulation in pandas, https://towardsdatascience.com/basic-time-series-manipulation-with-pandas-4432afee64ea
* Facebook Prophet quick-start guide: https://facebook.github.io/prophet/docs/quick_start.html#python-api
* AQI lookup table: http://www.sparetheair.com/publications/AQI_Lookup_Table-PM25.pdf
* AQI calculation: https://metone.com/how-to-calculate-aqi-and-nowcast-indices/
* timeanddate historical weather data: https://www.timeanddate.com/weather/chile/santiago/historic?month=8&year=2020
* How to display altair plot in Flask: https://github.com/xofbd/sql-viz-project/blob/minimal-app/app/app.py
