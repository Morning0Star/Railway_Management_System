from models import Booking, Train

def find_user_bookings(db, user_id):
    return db.query(Booking).join(Train).filter(
        Booking.user_id == user_id
    ).all()

def find_booking_by_id(db, booking_id, user_id):
    return db.query(Booking).join(Train).filter(
        Booking.id == booking_id,
        Booking.user_id == user_id
    ).first()

def create_booking(db, train_id, user_id):
    booking = Booking(
        train_id=train_id,
        user_id=user_id
    )
    db.add(booking)
    db.commit()
    return booking

def delete_booking(db, booking_id, user_id):
    return db.query(Booking).filter(
        Booking.id == booking_id,
        Booking.user_id == user_id
    ).delete() 