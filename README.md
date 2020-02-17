![Stellio](https://raw.githubusercontent.com/iam-abbas/Stellio/master/static/Stellio.png)

### Stellio is a flight Booking Platform which also serves as a tour suggestion system. 
The main target audience of Stellio would be people who do not mind having long layovers for a cheaper price. They can book a tour in the same city as their layover and have a tremendous experience. We make suggestions based on factors like:- 
- Time of Travel
- Duration of Layovers
- Age
- Interest Areas
- Previous Experiences
- Reviews
We plan to add more factors in the future. Our platform can also be integrated on any trip booking site(Cheapflights, uber). We also have a feature where you can try out free food samples from different restaurants on your way.

## Technical Report

### Technologies used
- Python
- Amadeus API (Sponsored)
- TomTom API (Sponsored)
- HTML/CSS
- JavaScript
- Jinjja

### Modules used
- Flask
- Amadeus Python SDK
- TomTom Web SDK
- ISO8601 Parser
- Date Parser
- Json

### How is Stellio built?

#### Flight System
The Backend of Stellio is built entirely on Flask. The flight data is fetched in real time from amadeus developer api. When you search for a flight a GET request is sent to ```/search``` which uses the following information to make an API call:-
- Origin City (string)
- Destinations City (string)
- Date of Travel (date)
- Number of Adults (int)
After the API call is made the response data is stored in a JSON object and is passed on to the rendered html template. Here Jinjja is used to display the required information from the json dictionary. JSON dictionary primarily includes:-
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
  - Manually made a Dictionary of known City's and their IATA Codes
  - Used IATA codes to map with the City names
 - Duration of Flight
 - Duration of Layover
 - Duration of Each Flight
 
 #### Tour System
 We used Points of Interest API (available from both Amadeus and TomTom) to point out most visited places in the given city and made a calculated route using TomTom's API using time constraints and then the Map is displayed using JavaScript on a different page.
 
 
 #### User Interface
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_2.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_4.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_6.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_7.png)
 ![](https://raw.githubusercontent.com/iam-abbas/Stellio/master/images/Screenshot_9.png)
 
 We would like to give Credits to:-
 - Colorlib (Bootstrap Snippets)
 - [Simon Matzinger](https://unsplash.com/@8moments) (Backgrounds)
 - [Nunki.com](https://www.nunki.com) (Javascript and CSS dependencies)
 
 ### Future Plans
 - As of now I do not have any plans
 
 ## How to use it?
 
 - fork this repository or clone it from ```https://github.com/iam-abbas/Stellio.git```
 - installing following using PIP
  - amadeus
  - iso8601
  - twilio
  - json
  - flask
 - Get the following APIs:-
  - Amadeus Free API
  - Twilio Free Trial Whatsapp API
  - TomTom Free API
 - Update ```main.py``` with your API keys where it is mentioned
 - For TomTom update it on ```/templates/map.html```
 - Now just run it using ```python3 main.py```
 
 ### License
 
 This project is licensed under MIT license feel free to use it how ever you want but make sure you give credits to creators.
 
 ## Accomplishments 
 
 #### Winner At DeveloperWeek 2020
 - We won sponsored first prize by Amadeus



