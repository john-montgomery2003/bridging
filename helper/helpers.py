# This helpers file makes the main code tidier, by creating a set of procedures/functions designed to perform the simpler tasks

import constant

################### PROCEDURES ###################

def acceptDetails():
	# Takes the question list as an argum
	# Uses list comprehension in order to take the inputs, returns as a class "car"
	inputs=[]
	for question in constant.questions:
		inputs.append(input(question))
	return constant.car(inputs[0],inputs[1],inputs[2],inputs[3],inputs[4])

def validateInput(inList):
	# Function which will perform tests on the inputs to check they are as expected
	# Performs type, length and pressence checks
	# The zip returns a consecutive pair of values from the list, eg (list1[0],list2[0]),(list1[1],list2[1]), etc
	returnString= ''
	for inputed,expected in zip(list(inList),constant.expectedForm):
		# True if the data was not in the expected format
		# True if the data was not in the expected length or not present
		errorLength = False if (len(str(inputed))>expected[1] or len(str(inputed))==0) else True
		if errorLength==False:
			#Returns the place of the error
			returnString = returnString + str(inputed) + '-'
	# Returns Empty string if no issues are present
	return returnString[:-1]

def calculateDiscount(carDetail):
	# carDetails is of type class
	discount = 0
	carDetail.cost,carDetail.year,carDetail.emissions=int(carDetail.cost),int(carDetail.year),int(carDetail.emissions)
	if carDetail.year<2016 and carDetail.emissions<4:
		discount += carDetail.cost*0.02
	if carDetail.model == "BMW":
		discount += carDetail.cost*0.05
	else:
		discount += carDetail.cost*0.03
	return round(discount, 2)

def calculateAddition(carDetail):
	# carDetails is of type class
	addition = 0
	if "Silver Paint" in carDetail.extra:
		addition += carDetail.cost * 0.06
	if "Alloy Wheels" in carDetail.extra:
		addition += carDetail.cost * 0.05
	return round(addition, 2)

def calculateFinal(cost, discount, addition):
	#performs the maths to calculate, purely to keep the code neater
	return (cost - discount + addition)

def comission(priceList, carDetail):
	#Both classes, one regards prices, one on car details
	comission = 0
	if carDetail.model.lower() == "citroen":
		comission += carDetail.cost * 0.02
	else:
		comission += carDetail.cost * 0.01
	comission += priceList.addition * 0.05
	return comission
