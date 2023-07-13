**imdb-movie-recommendation-tool**

Unlike other forms of media I consume, I don't really have a record of what film's I've seen, and when struggling for something to watch I came up with the idea to (hopefully) automate that decision. 

Therefore, I decided to create a simple spreadsheet to collate the films I've watched. An apple script is utilised to convert an apple numbers file containing this information to a CSV, so it can be inputted into a SQLite database for model development. 

Whilst a great open api exists (kudos to those at https://www.omdbapi.com/), I decided to use selenium and beautiful soup to scrape information for 500 films on the imdb database due to the fact that more information is available. 

For context, these are the datapoints available on the api: 

Description
IMDb ID 
Movie title 
Type of result to return.
Year of release.
plot.

Whereas our script creates the following information:
1. `runtime`: The runtime of the movie
2. `age_rating`: The age rating of the movie
3. `release_year`: The release year of the movie
4. `metascore`: The metascore of the movie
5. `awards`: The awards that the movie received
6. `director`: The director of the movie
7. `writers`: The writers of the movie
8. `stars`: The stars of the movie
9. `storyline`: The storyline of the movie
10. `genre`: The genre of the movie
11. `country_of_origin`: The country of origin of the movie
12. `language`: The language of the movie
...

Selenium is used to automate the collection of html data, which is then parsed using a mixture of beautifulsoup and regex to remove javascript and CSCS information for quick and easy analysis. 

Moreover I intend to scrape reviews, although this will be given significantly less weight in the model than reviews by critics. 

There is a view to also scrape other famous movie dbs to provide a more comprehensive model, vs. simply just using imdb. 





