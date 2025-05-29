from services.booking_service import (
    find_user_bookings,
    find_booking_by_id,
    create_booking as create_booking_service,
    delete_booking
)
from services.train_service import (
    find_train_by_id_for_update,
    count_booked_seats
)
from utils.errors import NotFoundError, BadRequestError

def get_user_bookings(db, user_id):
    bookings = find_user_bookings(db, user_id)
    
    return [{
        'id': booking.id,
        'trainId': booking.train_id,
        'trainName': booking.train.name,
        'source': booking.train.source,
        'destination': booking.train.destination,
        'createdAt': booking.created_at
    } for booking in bookings]

def get_booking_by_id(db, booking_id, user_id):
    booking = find_booking_by_id(db, booking_id, user_id)
    
    if not booking:
        raise NotFoundError("Booking not found")
        
    return {
        'id': booking.id,
        'trainId': booking.train_id,
        'trainName': booking.train.name,
        'source': booking.train.source,
        'destination': booking.train.destination,
        'createdAt': booking.created_at
    }

def create_booking(db, train_id, user_id):
    train = find_train_by_id_for_update(db, train_id)
    if not train:
        raise NotFoundError("Train not found")
        
    booked_seats = count_booked_seats(db, train_id)
    
    if booked_seats >= train.total_seats:
        raise BadRequestError("No seats available")
        
    return create_booking_service(db, train_id, user_id)

def cancel_booking(db, booking_id, user_id):
    result = delete_booking(db, booking_id, user_id)
    
    if result == 0:
        raise NotFoundError("Booking not found")
        
    db.commit() 