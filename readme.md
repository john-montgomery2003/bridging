# Bridging to A-Level #

The code documented here is for the current (master) branch, which has an optional GUI and postgreSQL database.

A sample DB is hosted on Heroku and contains some sample data.

### Basic Functionality ###

As standard the code runs in non-GUI (txt) with storage to a CSV file. In the `constants.py` file it is possible to change this as required.

The program will prompt for the inputs:
* model
* cost
* year
* emissions
* extras

The values are then converted to car type, and a price list is generated and outputted.

The program will then ask whether it should save this data, if yes it takes the name of the salesperson.

It is then stored into the DB or CSV.


![Image of Menu](/images/menu.png)

![Image of Add Car](/images/addCar.png)

![Image of View Car](/images/viewCar.png)

![Image of View Sales](/images/viewSales.png)

### GUI Functionality ###

If the GUI is activated then a window will pop up, this primarily acts as a menu. The page has 3 buttons redirecting to 2 view pages and 1 form. The user can view car or sales data. The form allows entry into the elected storage media.


### Other Constants ###

The constants file also has the ability to adjust:
* The questions asked to the user
* The data validation
* The string format of the car and price data
* Database URI
