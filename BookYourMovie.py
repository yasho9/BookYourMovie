
class BookYourMovies:
    tickets=[]
    bookedSeat={}

    currentIncome=0
    def MakeTheTickets(self):
        for i in range(self.rows+1):
            b = []
            for j in range(self.columns+1):
                if i == 0 and j == 0:
                    b.append(" ")
                elif i == 0:
                    b.append(j)
                elif j == 0:
                    b.append(i)
                else:
                    b.append("S")
            self.tickets.append(b)
        print()
        for i in range(len(self.tickets)):
            for j in range(len(self.tickets[0])):
                print(self.tickets[i][j], end=" ")
            print()
        print()

    def ShowTheTickets(self):
        print()
        for i in range(len(self.tickets)):
            for j in range(len(self.tickets[0])):
                print(self.tickets[i][j], end=" ")
            print()
        print()

    def BuyTickets(self):
        x = input("Enter the Row Number Where you want to buy a ticket ")
        y = input("Enter the Column Number Where you want to buy a ticket ")
        self.x = int(x)
        self.y = int(y)
        total_seats = self.rows*self.columns
        if total_seats>60:
            if (self.rows//2) <= self.x:
                self.price_of_seats = 10
                print(self.price_of_seats,'$ ')
            else:
                self.price_of_seats = 8
                print(self.price_of_seats,'$ ')
        else:
            self.price_of_seats = 10
            print("Price of Seat is ",self.price_of_seats, '$')

        book=input("Do you want to book a ticket ?? Yes/No ?? ")
        if book == "Yes":
            if total_seats > 60:
                if (self.rows // 2) <= self.x:
                    self.price_of_seats = 10
                    self.currentIncome += self.price_of_seats
                else:
                    self.price_of_seats = 8
                    self.currentIncome += self.price_of_seats
            else:
                self.price_of_seats = 10
                self.currentIncome += self.price_of_seats
            info = {}
            name=input("Enter your name: ")
            info['name']=name
            gender=input("Enter Gender M or F: ")
            info['Gender'] = gender
            age=int(input("Enter Age: "))
            info['Age'] = age
            number=int(input("Enter Phone Number: "))
            info['Phone_no'] = number
            info['ticket_price'] = self.price_of_seats
            self.bookedSeat[str(self.x) + str(self.y)] = info
            self.tickets[self.x][self.y] = "B"

            print("TICKET BOOKED SUCCESSFULLY ")
        else:
            print()
            print("Have a Happy Day....!!! ")


        print()

    def Statistics(self):
        self.count = 0
        for i in range(len(self.tickets)):
            for j in range(len(self.tickets[0])):
                if self.tickets[i][j] == "B":
                    self.count+=1
        print("Purchased tickets are:",self.count)
        total_seats = self.rows * self.columns
        self.PercetangeOfBookedTickets = (self.count/total_seats)*100
        print("Percentage of Booked tickets is:", int(self.PercetangeOfBookedTickets),"%")
        print("Current Income:",self.currentIncome,"$")
        total_seats = self.rows * self.columns
        if total_seats<=60:
            self.totalIncome = (self.rows*self.columns)*10
        else:
            half1 = self.rows//2
            half_1=self.columns//2
            half2 = self.rows-half1
            half_2=self.columns-half_1
            self.totalIncome = (half1*half_1*10)+(half2*half_2*8)
        print("Total Income: ",self.totalIncome,"$")
        print()

    def UserInfo(self):
        a = int(input("Enter the row of Booked Ticket "))
        b = int(input("Enter the column of Booked Ticket "))
        if self.tickets[a][b] == "B":
            print("Name:",self.bookedSeat[str(a)+str(b)]['name'])
            print("Gender:",self.bookedSeat[str(a) + str(b)]['Gender'])
            print("Age:",self.bookedSeat[str(a) + str(b)]['Age'])
            print("Ticket Price:",self.bookedSeat[str(a) + str(b)]['ticket_price'])
            print("Phone Number:",self.bookedSeat[str(a) + str(b)]['Phone_no'])
            print()
        else:
            print("Ticket is not Booked Yet")


