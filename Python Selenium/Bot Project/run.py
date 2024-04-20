from booking.booking import Booking
#    package file name      classname


# inst = Booking() #creating an instance
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    # print("Exiting...")
    bot.change_currency(currency='USD')
