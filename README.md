#### Crime_san
##### Crime data in San Francisco between 01/01/2015 to 31/03/2015

##### Submit1:  
1. Parse the data and change from csv type to database.  
2. Build basic system on MVC structure.  
3. Add two basic search functions and one overview function:  
  * Date search  
  * Position search  
  * One table overview function.  
(submit on 01/03/2022)  

##### Submit2:  
1. Restructure the database and tables to make the data lists more reasonable.  
2. Add Try-except function to avoid wrong or unexpected data, or other error happen perheps.  
3. Add one accurate search function by inputing coordinates.  
(submit on 03/03/2022)

##### Submit3:  
1. Add a behave test.  
2. Connect and test with Heroku  
(submit on 04/03/2022)


Report part:
#### Data source
In this task, I choose a crime in San Francisco happened in the first 3 months in 2015, which contains more than 20000 rows of data and 6 column  for each row.
#### Data parse
To make the app more powerful with multi-function, I generated two linked tables. One inherits the date information mainly, and it also is the basic source for building a search system by matching date. The other table inherits the exact and accurate address, even the coordinates, so it devotes to the position-search part.
#### Development
Not only the two search function mentioned, but a coordinate search is provided. This function allows the user to enter a couple of number including longitude and latitude to match the crime events happened around there. The system is flexible, and various accuracy floating numbers are available, which will influence the accuracy of the result definitely. More exact and accurate coordinates means more digit number in floating, leads to more accurate and less result.
#### What’s more in development
To avoid error data, there is an error handling part in code, so that the app could prevent to crash down when an unexpected data occurred.
To ensure the app could run smoothly and successfully with less and even no bug as expected. A behave test is added.
All work and files have been uploaded to github to achieve version tracking and control.
The app could be run on Heroku so that it ensures everyone could use it.
