import user_functions
con_in = "y"

while con_in == "y" or con_in =="Y":
    print("INDIAN RAILWAY TICKET RESERVATION SYSTEM")
    print("****************************************")
    print("1. Ticket Booking")
    print("2. Ticket Canceling")
    print("3. Booked ticket Status")
    print("4. Exit")
    input1 = int(input("Enter your choice :"))

    if input1 == 1:
        user_functions.book_ticket()
        # check = input("To exit press n.:")
        # if check == "n":
        #     exit()
    elif input1 == 2:
        ticket_no = int(input("Enter the Ticket No: "))
        user_functions.cancel_ticket(ticket_no)
    elif input1 ==3 :
        ticket_no = input("Enter the Ticket No: ")
        user_functions.ticket_status(ticket_no)
    elif input1 == 4:
        exit()
    else:
        print("Invalid Operation")
        con_in = input("Do you wish to continue,press y.\npress any other key to exit :")
