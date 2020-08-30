### Import required modules ###

#These are the 2 modules from the directory
import constant, helper

import csv
from tabulate import tabulate
from tkinter import *
from tkinter import ttk
from functools import partial
<<<<<<< HEAD
import sys
=======
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c

#If the constant file is set to use a DB for storage then this will trigger
#It connects to the DB, and then executes 2 postgreSQL commands
#These commands ensure that the tables are created in the database
#The URI of said database is accessable from the constants file
<<<<<<< HEAD
if not sys.argv[1].lower()=="csv":
=======
if not constant.csv:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    #Importing the required SQL alchemy modules to set up the DB only needed when running in DB mode
    from sqlalchemy import create_engine
    from sqlalchemy.orm import scoped_session, sessionmaker

    #Connecting to the corrects server
    engine = create_engine(constant.dbURI)
    db = scoped_session(sessionmaker(bind=engine))

    # Creates table "car" this stores data about the car
    db.execute("""CREATE TABLE IF NOT EXISTS "car" (
"id" serial NOT NULL,
"model" character varying NOT NULL,
"cost" integer NOT NULL,
"year" integer NOT NULL,
"emissions" integer NOT NULL,
"extras" character varying NOT NULL,
"discount" integer NOT NULL,
"addition" integer NOT NULL,
"final" integer NOT NULL,
"salesperson" character varying NOT NULL
);""")
    # Creates table "salesperson" this stores data about the salespeople
    db.execute("""CREATE TABLE IF NOT EXISTS "salesperson" (
"id" serial NOT NULL,
"name" character varying NOT NULL,
"total" integer NOT NULL,
"salesValue" integer NOT NULL,
"numberOfSales" integer NOT NULL
);""")

    #Commits changes to the database
    db.commit()

"""
  _   _    ___    _   _                ____   _   _   ___
 | \ | |  / _ \  | \ | |              / ___| | | | | |_ _|
 |  \| | | | | | |  \| |    _____    | |  _  | | | |  | |
 | |\  | | |_| | | |\  |   |_____|   | |_| | | |_| |  | |
 |_| \_|  \___/  |_| \_|              \____|  \___/  |___|

"""
#This is the function that runs when the user selects to run in the txt viewCar
def nonGUI():
    #Looped to allow multiple cars to be added easily
    while True:
        #Essentially the menu
        choice = input("Would you like to view the data or add a car or view your sales or quit [view/add/sales/quit] - ").lower()
        #If user elects to add a new car
        if choice == 'add':
            #Loops until an acceptable set of inputs has been provided
            #This is controlled by the validator function in helper.py
            while True:
                carDetails = helper.acceptDetails()
                validator = helper.validateInput(carDetails)
                if validator:
                    #Prints error and allows user to see issue
                    print("-- ERROR WITH INPUT --")
                    print(validator)
                else:
                    #Once an acceptable set is inputed
                    break
            #Calculates the discount
            discount = helper.calculateDiscount(carDetails)
            #Calculates the addition
            addition = helper.calculateAddition(carDetails)
            #Calculates the final
            final = helper.calculateFinal(carDetails.cost, discount, addition)
            #Generates a pricelist with the class `priceList`
            priceList = constant.priceList(discount, addition, final)
            #Calculates the comission
            comissionAmount = round(helper.comission(priceList, carDetails), 2)
            #Outputs the inputs and calculated valuse
            #Must be cast to string to take advantage of the classes __str__
            print(str(carDetails))
            print(str(priceList))
            print(f"(Comission => {comissionAmount})")
            #Checks the user wants to save this car, or just calculate the values
            if input("Would you like to save this car [y/n] - ").lower() == 'y':
                #Requests a name to store the car under
                salesPerson = input("Enter your name - ")
                #Checks if storage is in csv or DB
<<<<<<< HEAD
                if sys.argv[1].lower()=="csv":
=======
                if constant.csv:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
                    #Writes data to the CSV
                    #Fisrt the data for the car
                    csvWriter = csv.writer(open('carSales.csv', 'a'))
                    csvWriter.writerow([carDetails.model,carDetails.cost,carDetails.year,carDetails.emissions,carDetails.extra,priceList.discount, priceList.addition, priceList.final, salesPerson])
                    #Then the data for the salesperson
                    readerData = list(csv.reader(open('salesData.csv')))
                    #first check that they dont already exist
                    found = False
                    for i in range(len(readerData)):
                        if readerData[i][0] == salesPerson:
                            #If they do already exst then add the data to the old data
                            found = True
                            readerData[i][1] = int(readerData[i][1]) + comissionAmount
                            readerData[i][2] = int(readerData[i][2]) + priceList.final
                            readerData[i][3] = int(readerData[i][3]) + 1
                            writer = csv.writer(open('salesData.csv', 'w'))
                            writer.writerows(readerData)
                    if not found:
                        #Otherwise add them to the file
                        writer = csv.writer(open('salesData.csv', 'a'))
                        writer.writerow([salesPerson, comissionAmount,priceList.final,1])
                else:
                    #Add car to the database
                    db.execute("INSERT INTO car (model, cost, year,emissions,extras, discount, addition, final, salesperson) VALUES (:model, :cost, :year, :emissions, :extras, :discount, :addition, :final, :salesperson)",
                        {"model": carDetails.model, "cost": carDetails.cost, "year": carDetails.year, "emissions": carDetails.emissions, "extras": carDetails.extra, "discount": priceList.discount, "addition": priceList.addition, "final": priceList.final, "salesperson": salesPerson})
                    db.commit()
                    #Commit this change (commited now as contingency incase of accidental disconnect, etc)
                    line = db.execute("SELECT * FROM salesperson WHERE name = :salesperson", {"salesperson":salesPerson}).fetchone()
                    #Check for data
                    if line != None:
                        line = list(line)
                        db.execute("UPDATE salesperson SET  total= :comission, salesValue = :final, numberOfSales = :salesCount WHERE name = :salesperson;", {"comission" :line[2]+comissionAmount , "final":line[3]+ priceList.final , "salesCount": line[4]+1, "salesperson" : salesPerson})
                    else:
                        db.execute("INSERT INTO salesperson (name,total,salesValue,numberOfSales) VALUES (:name, :total, :salesValue, :numberOfSales)", {"name" : salesPerson, "total":comissionAmount, "salesValue": priceList.final, "numberOfSales":1})
                    db.commit()
        #If the user elected to view the data instead
        elif choice == 'view':
            #get the data from whereever it currently exists
<<<<<<< HEAD
            if sys.argv[1].lower()=="csv":
=======
            if constant.csv:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
                #print the heading
                print('\nCAR DATA\n')
                #Pull the data, and use tabulate to generate an ASCII table for displaying
                data = list(csv.reader(open('carSales.csv')))
                print(tabulate(data,headers="firstrow",tablefmt="grid"))
                #print the heading
                print('\nSALES DATA\n')
                #Pull the data, and use tabulate to generate an ASCII table for displaying
                data = list(csv.reader(open('salesData.csv')))
                print(tabulate(data,headers="firstrow",tablefmt="grid"))
            else:
                #Pull the data from the DB
                carData = list(db.execute("SELECT * FROM car").fetchall())
                #print the heading
                print('\n CAR DATA \n')
                #Use tabulate to generate an ASCII table for displaying
                print(tabulate(carData,headers=["id","Model","Initial Price","Year","Emissions","Extras","Discount","Addition","Final Price","Salesperson"],tablefmt="grid"))
                #print the heading
                print('\nSALES DATA\n')
                #Pull the data, and use tabulate to generate an ASCII table for displaying
                data = list(db.execute("SELECT * FROM salesperson").fetchall())
                print(tabulate(data,headers=["id","name","Comission","Sales Total","Sales"],tablefmt="grid"))
        #If the user elected to see the sales data
        elif choice == 'sales':
<<<<<<< HEAD
            if sys.argv[1].lower()=="csv":
=======
            if constant.csv:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
                #Pull the data from the CSV
                data = list(csv.reader(open('salesData.csv')))
                #print the heading
                print('\n SALES DATA \n')
                #Use tabulate to generate an ASCII table for displaying
                print(tabulate(data,headers="firstrow",tablefmt="grid"))
            else:
                #Pull the data from the DB
                data = list(db.execute("SELECT * FROM car WHERE salesperson = :name", {"name":input('Enter the name of the salesperson - ')}).fetchall())
                #print the heading
                print('\n SALES DATA \n')
                #Use tabulate to generate an ASCII table for displaying
                print(tabulate(data,headers=["id","Model","Initial Price","Year","Emissions","Extras","Discount","Addition","Final Price","Salesperson"],tablefmt="grid"))
        #Allows the user to quit the program, will do so too if the text was not one of the 3 options
        else:
            exit()

"""
   ____   _   _   ___
  / ___| | | | | |_ _|
 | |  _  | | | |  | |
 | |_| | | |_| |  | |
  \____|  \___/  |___|

"""

def homePage():
    #Main home page of the app, shows 3 buttons, allowing rediect to other pages
    root = Tk()
    canvas = Canvas(root, width = 400, height = 300)
    canvas.pack()
    #Sets up title, sub title and buttons
    title = Label(root, text='Car Inventory')
    title.config(font=('helvetica', 30))
    canvas.create_window(200, 25, window=title)

    subTitle = Label(root, text='Select an option:')
    subTitle.config(font=('helvetica', 10))
    canvas.create_window(200, 100, window=subTitle)

    viewCar = Button (text = "View Cars", command = viewCarPage ,width = 12)
    viewCar.place(x = 150,y = 110)

    viewSales = Button (text = "View Sales", command = viewSalePage,width = 12)
    viewSales.place(x = 150,y = 135)

    #partial has to be used here to create the function so it can be called without parameters
    #This is because the command in Button doesnt support parsing parameters
    add_Page=partial(addPage, "")
    addCar = Button (text = "Add Car", command=add_Page, width = 12)
    addCar.place(x = 150,y = 160)

    root.mainloop()

#This page will show a table of the cars
def viewCarPage():
    #Grab the data for the car
<<<<<<< HEAD
    carData = list(csv.reader(open('carSales.csv')))[1:] if sys.argv[1].lower()=="csv" else list(db.execute("SELECT * FROM car").fetchall())
=======
    carData = list(csv.reader(open('carSales.csv')))[1:] if constant.csv else list(db.execute("SELECT * FROM car").fetchall())
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    #Set up tkinter
    root = Tk()

    #Define the table headers
<<<<<<< HEAD
    if not sys.argv[1].lower()=="csv":
        head = ["ID","Model","Initial Price","Year","Emissions","Extras","Discount","Addition","Final Price","Salesperson"]
    else:
        head = ["Model","Initial Price","Year","Emissions","Extras","Discount","Addition","Final Price","Salesperson"]
=======
    head = ["id","Model","Initial Price","Year","Emissions","Extras","Discount","Addition","Final Price","Salesperson"]

>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    #treeview allows the generation of a table in tk
    treeview = ttk.Treeview(root)
    treeview.grid(columnspan=10)
    treeview["columns"] = head
    treeview["show"] = "headings"
    for val in head:
        treeview.heading(val, text=val)
        treeview.column(val, minwidth=0, width=120)
    index, iid = 0, 0
    for val in carData:
        treeview.insert("", index, iid, values=tuple(val))
        index +=1
        iid+=1
    root.mainloop()

#Similar to viewCarPage this funtion shows a window with the data for the salespeople instead
def viewSalePage():
    #Grab the data for the car
<<<<<<< HEAD
    salesData = list(csv.reader(open('salesData.csv')))[1:] if sys.argv[1].lower()=="csv" else list(db.execute("SELECT * FROM salesperson").fetchall())
=======
    salesData = list(csv.reader(open('salesData.csv')))[1:] if constant.csv else list(db.execute("SELECT * FROM salesperson").fetchall())
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    #Set up tkinter
    root = Tk()

    #Define the table headers
<<<<<<< HEAD
    if not sys.argv[1].lower()=="csv":
        head = ["ID","Name","Total Comission","Value Sold","Cars Sold"]
    else:
        head = ["Name","Total Comission","Value Sold","Cars Sold"]
=======
    head = ["id","Name","Total Comission","Value Sold","Cars Sold"]
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    #treeview used to generate a table in tk
    treeview = ttk.Treeview(root)
    treeview.grid(columnspan=9)
    treeview["columns"] = head
    treeview["show"] = "headings"
    for val in head:
        treeview.heading(val, text=val)
        treeview.column(val, minwidth=0, width=120)
        index, iid = 0, 0
    for val in salesData:
        treeview.insert("", index, iid, values=tuple(val))
        index +=1
        iid+=1
    root.mainloop()

#Function that adds data based on the inputs
#must take the buttons as params
def addData(modelIn1,modelIn2,modelIn3,modelIn4,modelIn5,modelIn6):
    #Get inputs once submit is pressed
    x1,x2,x3,x4,x5 = (modelIn1.get()),(modelIn5.get()),(modelIn2.get()),(modelIn3.get()),(modelIn4.get())
    #Create a car object
    carData = constant.car(x1 , x2,x3,x4,x5)
    #Get inputed sales person
    salesPerson = modelIn6.get()

    #Validate inputs
    validator = helper.validateInput(carData)
    if validator:
        #Display bassic error page, no context passed in here
        root = Tk()
        canvas = Canvas(root, width = 400, height = 300)
        canvas.pack()

        title = Label(root, text='Error with Inputs')
        title.config(font=('helvetica', 30))
        canvas.create_window(200, 25, window=title)

        root.mainloop()

    else:
        #Store data
        discount = helper.calculateDiscount(carData)
        addition = helper.calculateAddition(carData)
        final = helper.calculateFinal(carData.cost, discount, addition)
        priceList = constant.priceList(discount, addition, final)
        comissionAmount = round(helper.comission(priceList, carData), 2)
<<<<<<< HEAD
        if sys.argv[1].lower()=="csv":
=======
        if constant.csv:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
            csvWriter = csv.writer(open('carSales.csv', 'a'))
            csvWriter.writerow([carData.model,carData.cost,carData.year,carData.emissions,carData.extra,priceList.discount, priceList.addition, priceList.final, salesPerson])
            readerData = list(csv.reader(open('salesData.csv')))
            found = False
            for i in range(len(readerData)):
                if readerData[i][0] == salesPerson:
                    found = True
                    readerData[i][1] = int(float(readerData[i][1])) + comissionAmount
                    readerData[i][2] = int(float(readerData[i][2])) + priceList.final
                    readerData[i][3] = int(readerData[i][3]) + 1
                    writer = csv.writer(open('salesData.csv', 'w'))
                    writer.writerows(readerData)
            if not found:
                writer = csv.writer(open('salesData.csv', 'a'))
                writer.writerow([salesPerson, comissionAmount,priceList.final,1])
            #Display the addPage again, with the message data added
            addPage("Data Added")
        else:
            global db
            db.execute("INSERT INTO car (model, cost, year,emissions,extras, discount, addition, final, salesperson) VALUES (:model, :cost, :year, :emissions, :extras, :discount, :addition, :final, :salesperson)",
                {"model": carData.model, "cost": carData.cost, "year": carData.year, "emissions": carData.emissions, "extras": carData.extra, "discount": priceList.discount, "addition": priceList.addition, "final": priceList.final, "salesperson": salesPerson})
            db.commit()
            line = db.execute("SELECT * FROM salesperson WHERE name = :salesperson", {"salesperson":salesPerson}).fetchone()
            if line != None:
                line = list(line)
                db.execute("UPDATE salesperson SET  total= :comission, salesValue = :final, numberOfSales = :salesCount WHERE name = :salesperson;", {"comission" :line[2]+comissionAmount , "final":line[3]+ priceList.final , "salesCount": line[4]+1, "salesperson" : salesPerson})
            else:
                db.execute("INSERT INTO salesperson (name,total,salesValue,numberOfSales) VALUES (:name, :total, :salesValue, :numberOfSales)", {"name" : salesPerson, "total":comissionAmount, "salesValue": priceList.final, "numberOfSales":1})
            db.commit()
            #Display the addPage again, with the message data added
            addPage("Data Added")


#The form for data input
def addPage(message):
    #shows a page for adding the data
    pageAdd = Tk()
    canvas = Canvas(pageAdd, width = 300, height = 300)
    title = Label(pageAdd, text='Add Car')
    title.config(font=('helvetica', 30))
    canvas.create_window(150, 25, window=title)
    #Will display a message if not "" or None
    if message:
        subtitle = Label(pageAdd, text=message)
        subtitle.config(font=('helvetica', 10), fg = "black")
        canvas.create_window(150, 50, window=subtitle)

    #Label values for input form
    inText = ("Model:", "Year:", "Emissions:", "Extras:", "Cost:", "Salesperson:")
    for i in range(len(inText)):
        labels = Label(pageAdd, text=inText[i])
        canvas.create_window(50, 90+(i*30), window=labels)

    #Input forms
    modelIn1 = Entry(pageAdd)
    canvas.create_window(200, 90, window=modelIn1)
    modelIn2 = Entry(pageAdd)
    canvas.create_window(200, 120, window=modelIn2)
    modelIn3 = Entry(pageAdd)
    canvas.create_window(200, 150, window=modelIn3)
    modelIn4 = Entry(pageAdd)
    canvas.create_window(200, 180, window=modelIn4)
    modelIn5 = Entry(pageAdd)
    canvas.create_window(200, 210, window=modelIn5)
    modelIn6 = Entry(pageAdd)
    canvas.create_window(200, 240, window=modelIn6)

    canvas.pack()

    #Submit button
    add_Data = partial(addData,modelIn1,modelIn2,modelIn3,modelIn4,modelIn5,modelIn6)
    submit = Button(canvas, text='Submit', command=add_Data)
    submit.place(x=150, y=260)

    canvas.pack()
    pageAdd.mainloop()

"""
  ____    ____    ___  __     __  _____   ____       ____    ___    ____    _____
 |  _ \  |  _ \  |_ _| \ \   / / | ____| |  _ \     / ___|  / _ \  |  _ \  | ____|
 | | | | | |_) |  | |   \ \ / /  |  _|   | |_) |   | |     | | | | | | | | |  _|
 | |_| | |  _ <   | |    \ V /   | |___  |  _ <    | |___  | |_| | | |_| | | |___
 |____/  |_| \_\ |___|    \_/    |_____| |_| \_\    \____|  \___/  |____/  |_____|

"""
<<<<<<< HEAD
if sys.argv[2].lower()=='gui':
=======
if constant.gui:
>>>>>>> 98cd1702576650b482168ed2f53775bebc44710c
    homePage()
else:
    while True:
        nonGUI()
