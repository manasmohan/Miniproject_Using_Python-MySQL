import mysql.connector as con
import random

def confirm_Book_ticket(no,name,source,dest,cost,count,key):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )
    cur = mydb.cursor()
    sql ="INSERT INTO bookstatus(trainno,trainname,sourcestation,destinationstation,cost,seats,ticketno) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (no,name,source,dest,cost,count,key)
    cur.execute(sql,val)
    mydb.commit()
    mydb.close()
    print("Ticket Booking Confirmed")

def book_ticket():
    global tr_cost, tr_name, tr_no, tr_source, tr_dest, totalcost
    source = input("Enter the the source station :")
    destination = input("Enter the destination station: ")
    mydb = con.connect(
      host="localhost",
      user="root",
      password="52828378Jyo#",
      database="raildb"
    )

    cur = mydb.cursor()
    sql = "Select trainno, trainname, departuretime, arrivaltime, cost from traindata WHERE sourcestation = %s and destinationstation = %s "
    sour = (source,destination)
    cur.execute(sql,sour)
    result = cur.fetchall()

    for x in result:
        print(f"Train No:{x[0]}\nTrain Name:{x[1]}\n{x[2]}-----------------{x[3]} \n Ticket Price :{x[4]}")
        tr_no = x[0]
        tr_name= x[1]
        tr_source = x[2]
        tr_dest = x[3]
        tr_cost = x[4]
    mydb.close()

    count = int(input("How many tickets you want : "))
    p = int(input("Which one do you prefer \n1.General 2.Chaircar 3.Sleeper 4.AC coach \nEnter your choice : "))
    if p == 1:
        print(f"Ticket price: {tr_cost}")
        totalcost = tr_cost * count
        print(totalcost)
    elif p == 2:
        print(f"Ticket price: {tr_cost + 10}")
        totalcost = (tr_cost + 10) * count
        print(totalcost)
    elif p ==3 :
        print(f"Ticket price: {tr_cost + 20}")
        totalcost = (tr_cost+ 20) * count
        print(totalcost)
    elif p ==4 :
        print(f"Ticket price: {tr_cost + 50}")
        totalcost = (tr_cost + 50 )* count
        print(totalcost)
    else:
        pass

    user_prompt = input("Do you wish to continue?Press y \nPress n to exit:")
    if user_prompt == "n" or user_prompt =="N":
        print("Process Terminated")
    elif user_prompt == "y" or user_prompt =="Y":
        ticket_no = random.randint(10000,99999)
        print("Ticket no : ",ticket_no)
        confirm_Book_ticket(tr_no,tr_name,tr_source,tr_dest,totalcost,count,ticket_no)


def cancel_ticket(no):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )

    cur = mydb.cursor()
    sql = ("DELETE FROM bookstatus WHERE ticketno = %s")
    val = (no,)
    cur.execute(sql,val)
    mydb.commit()
    print("The ticket has been cancelled!!")

def ticket_status(no):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )

    cur = mydb.cursor()
    cur.execute(f"SELECT trainno,trainname,sourcestation,destinationstation,cost,seats,ticketno FROM bookstatus WHERE ticketno = {no}")
    val = cur.fetchall()
    for x in val:
        print(x)
    mydb.close()






