import BookYourMovie
if __name__ == '__main__':
    obj = BookYourMovie.BookYourMovies()
    print("_______________Book Your Movie _________________")
    print()
    obj.rows = int(input("Enter Number of Rows "))
    obj.columns = int(input("Enter Number of seats in each Row "))
    obj.MakeTheTickets()
    print()

    while( True ):
        print("1. Show the tickets ")
        print("2. Buy a tickets ")
        print("3. Statistics ")
        print("4. Show Booked tickets User Info ")
        print("0. Exit ")
        print()

        user_input = int(input())

        if user_input == 1:
            obj.ShowTheTickets()
        elif user_input == 2:
            obj.BuyTickets()
        elif user_input == 3:
            obj.Statistics()
        elif user_input == 4:
            obj.UserInfo()
        elif user_input == 0:
            break
        else:
            print(" Enter Valid Input ")
            print()



