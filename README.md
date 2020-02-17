![Stellio](https://raw.githubusercontent.com/iam-abbas/Stellio/master/static/Stellio.png)

### Stellio is a flight Booking Platform which also serves as a tour suggestion system. 
The main target audiance of Stellio would be people who do not mind having long layoivers for a cheaper price. They can book a tour in the same city as their layover and have a tremendous experiance. We make suggestions baded on factors like:- 
- Time of Travel
- Duration of Layovers
- Age
- Interest Areas
- Previous Experiances
- Reviews
We plan to add more factors in the future. Our platform can also be integrated on any trip booking site(Cheapflights, uber). We also have a feature where you can try out free food samples from different restaurants on your way.

## Technical Report

### Technologies used
- Python
- Amadeus API (Sponsored)
- TomTom API (Sponsored)
- HTML/CSS
- JavaScript
- Jjinja

### Modules used
- Flask
- Amadeus Python SDK
- TomTom Web SDK
- ISO8601 Parser
- Date Parser
- Json

### How is Stellio built?

#### Flight System
The Backend of Stellio is built entirely on Flask the flight dsta is fetched in realtime from amadeus developer api. When you search for a flight a GET request is sent to ```/search``` which uses the following information to make an API call:-
- Origin City (string)
- Destinations City (string)
- Date of Travel (date)
- Number of Adults (int)
After the API call is made the response data is store in a JSON object and is passed on to the rendered html template. Here Jjinja is used to display the required information from the json dictonary. JSON dictonary primirily includes:-
- IATA Codes of:
  - Origin City
  - Layover Cities
  - Destination City
 - Time and Dates (ISO 8601 Format) of:-
  - Departure at Origin
  - Arrival at Layover City(s)
  - Departure at Layover City(s)
  - Arrival at Destination
 - Flight Number
 - Carrier Code
 
###### Above Information is used to derive the following
- Name of the City
  - Manually made a Dictonary of know City's and their IATA Codes
  - Used IATA codes to map with the City names
 - Duration of Flight
 - Duration of Layover
 - Duration of Each Flight
 
 #### Tour System
 We used Points of Interest API (availble from both Amadeus and TomTom) to point out most visited places in the given city and made a calculated a route using TomTom's API using time constraints and then the Map is displayed using JavaScript on a diferent page.
 
 
 #### User Interface
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_2.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_4.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_6.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_7.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_9.png)
 
 We would like to give Credits to:-
 - Colorlib (Bootstrap Snippets)
 - [Simon Matzinger](https://unsplash.com/@8moments) (Backgrounds)
 - [Nunki.com](https://www.nunki.com) (Javascript and CSS dependancies)
 
 ### Future Plans
 - As of now I do not have any plans
 
 
 ## Accomplishments 
 
 #### Winner At DeveloperWeek 2020
 - We won sponsored first prize by Amadeus
