<<<<<<< HEAD
=======
#The constants file holds the values users may want to change, ie whether or not the program runs in GUI or not
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
#This could be controlled with __name__ but I found this to be a slightly more elegant approach
#As it allows the GUI to be used from terminal as well as an IDE


<<<<<<< HEAD
=======
#run in GUI or in text
gui = False

#save in CSV or DB
csv = True

>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
#DB URI (if using DB)
dbURI = "postgres://zvulcvbmreajwj:fc82588eee9a53d2f2a98d9697ad7711dbc89642a4b681352840a9f41e02ead8@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/dfsgomeafivhq2"


#Car class, formats inputed car data
class car:
	# Main class for a cars details
	def __init__(self, model, cost, year, emissions, extra):
	# Defines how the class values are referenced
		self.model = model
		self.year = year
		self.emissions = emissions
		self.extra = extra
		self.cost = cost

	#Defines what the class should format as when "str"
	def __str__(self):
		return """=============================================
MODEL 		--> {self.model}
YEAR  		--> {self.year}
EMISSIONS	--> {self.emissions}
EXTRAS		--> {self.extra}
INITIAL COST--> £{self.cost}.00s""".format(self=self)

	#Allows for iteration through the elements
	def __iter__(self):
		yield self.model
		yield self.cost
		yield self.year
		yield self.emissions
		yield self.extra

class priceList:
	#Secondary class for the price list
	def __init__(self, discount, addition, final):
	# Defines how the class values are referenced
		self.discount = discount
		self.addition = addition
		self.final = final

	#Defines what the class should look like on printing
	def __str__(self):
		return """- - - - -
DISCOUNT 	--> £{self.discount}
ADDITIONS	--> £{self.addition}
- - - - - - - - - - -
FINAL PRICE			--> £{self.final}""".format(self=self)


# For ease of use all questions are defined here, allowing the user to easily adjust the questions asked
questions = [
"Enter Car Model - ",
"Enter Car Cost - ",
"Enter Year of Manufacture - ",
"Enter Car Emissions - ",
"Does the car have any extras (if yes, list)? "]

# Expected format of the questions's inputs, the first value being the data type, the second the length, program also performs a presense check
# User friendly data types, where:
# text = str
# integer = int
#float = float
expectedForm = [
["text", 64],
["float", 10],
["integer", 4],
["integer", 2],
["text", 64]
]
