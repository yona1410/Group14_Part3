from mongodb import apartments_col,users_col,bookings_col

booking_records=bookings_col.find()

for booking_record in booking_records:
    print(booking_record)
print()
apartments_records=apartments_col.find()

for apartment_record in apartments_records:
    print(apartment_record)
print()
users_records=users_col.find()

for user_record in users_records:
    print(user_record)