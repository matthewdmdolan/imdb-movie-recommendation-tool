**imdb-movie-recommendation-tool**

Unlike other forms of media I consume, I don't really have a record of what film's I've seen, and when struggling for something to watch I came up with the idea to (hopefully) automate that decision. 
Therefore, I decided to create a simple spreadsheet to collate the films I've watched. An apple script is utilised to convert an apple numbers file containing this information to a CSV, so it can be inputted into a SQLite database to build a recommendation model that will apply different weights after a continuous development cycle. 

Whilst a great open api exists (kudos to those at https://www.omdbapi.com/), I decided to use selenium and beautiful soup to scrape information for 500 films on the imdb database due to the fact that more information is available. 

For context, these are the datapoints available on the api: 


By ID or Title
Parameter	Required	Valid Options	Default Value	Description
i	Optional*		<empty>	A valid IMDb ID (e.g. tt1285016)
t	Optional*		<empty>	Movie title to search for.
type	No	movie, series, episode	<empty>	Type of result to return.
y	No		<empty>	Year of release.
plot	No	short, full	short	Return short or full plot.
r	No	json, xml	json	The data type to return.
callback	No		<empty>	JSONP callback name.
v	No		1	API version (reserved for future use).*Please note while both "i" and "t" are optional at least one argument is required.


By Search
Parameter	Required	Valid options	Default Value	Description
s	Yes		<empty>	Movie title to search for.
type	No	movie, series, episode	<empty>	Type of result to return.
y	No		<empty>	Year of release.
r	No	json, xml	json	The data type to return.
page New!	No	1-100	1	Page number to return.
callback	No		<empty>	JSONP callback name.
v	No		1	API version (reserved for future use).

Whereas our script creates the following information:
...

Therefore Selenium is used to automate the collection of html data, which is then parsed using a mixture of beautifulsoup and regex to remove javascript and CSCS information for quick and easy analysis. 

Moreover I intend to scrape reviews, although this will be given significantly less weight than critical reviews.  

There is a view to also scrape other famous movie dbs to provide a more comprehensive model, vs. simply just using imdb. 





