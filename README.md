![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnB-SU3-O8yXNBMxIp5t5AqMhIpGZsg8myl51SKnKF3kY5wwAuKQ)

# League of Legends game winner prediction at 15 minutes

This project attempts to collect in-game League of Legends data using Riot Open API and use relevant information to perform prediction on the outcome of a match.

## File Description
 
 * League Project Main.ipynb - This is the main jupyter notebook that contains all the information from data crawwling to data analysis and Flask implementation.
 
 * flask_demo.py & league_flask.py - Both of these python files are used for quick Flask testing.
 
 * league_lor.pkl - This file contains serialized information about the Logistic Regression model that had the highest accuracy in the analysis.
 
 * match_detail_compile_total.csv - This file contains the final dataset that was used (Some additional preprocessing is performed in the main ipynb file).

## Data Selection

The main objective of the project was to come up with an improved model from the reference reddit project. For one thing, the reddit project utilizes data at 10 minute mark, which I believe is too early in the match. Additionally, I decided to only utilize game data from high tier players (top 0.1% players) because matches in lower tier are prone to issues such as trolling and unoptimized gameplay from individual players, and these game data will act as 'noise data'. 

To get around those issues, I choose 15 minute, when players can begin to surrender the match, game data for Challenger, Master, high Diamond 1 players from Korean server.

## Quick Summary

The most challenging portion was the data collection itself. Riot Open API does not provide one-way solution to gathering relevant data and it has to be done by sending multiple API requests. On top of that, for the free API account, the server has rate limits. For this reason, my data ended up with only around 17,500 data which is relatively a small dataset. However, I believe the methodology in which the analysis was carried out seems reasonable and that, with more time, one can collect a larger dataset and follow the same steps to carry out identical analysis.

EDA was carried out using Pymongo and Seaborn package. The models used to perform the analysis include Logistic Regression, Random Forest, XGBoost, AdaBoost, and BaggingClassifier. The accuracy of all models fell within 75~78% test accuracy with Logistic Regression being 1% higher than XGBoost or Random Forest.

As the final part of the project, a simple Flask server request for prototyping was also included.

## Useful References

* [Riot Open API](https://developer.riotgames.com/) -> Official Riot Open API
* [Reddit Reference Project](https://www.reddit.com/r/MachineLearning/comments/4vdsg4/predicting_the_winner_of_a_league_of_legends/) -> The outline of the current project was based on this reddit thread and the git address provided in the thread.

## Acknowledgments

This project was done as a part of Final Portfolio for FastCampus Data Science coding camp.
