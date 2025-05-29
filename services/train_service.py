from sqlalchemy import func
from models import Train, Booking

def find_all_trains(db):
    return db.query(
        Train,
        (Train.total_seats - func.count(Booking.id)).label('available_seats')
    ).outerjoin(Booking).group_by(Train.id).all()

def find_trains_by_route(db, source, destination):
    return db.query(
        Train,
        (Train.total_seats - func.count(Booking.id)).label('available_seats')
    ).outerjoin(Booking).group_by(Train.id).filter(
        Train.source == source,
        Train.destination == destination
    ).all()

def find_train_by_id(db, train_id):
    return db.query(Train).filter(Train.id == train_id).first()

def find_train_by_id_for_update(db, train_id):
    return db.query(Train).filter(Train.id == train_id).with_for_update().first()

def create_train(db, train_data):
    train = Train(
        id=train_data['id'],
        name=train_data['name'],
        source=train_data['source'],
        destination=train_data['destination'],
        total_seats=train_data['totalSeats']
    )
    db.add(train)
    db.commit()
    return train

def count_booked_seats(db, train_id):
    return db.query(func.count(Booking.id)).filter(
        Booking.train_id == train_id
    ).scalar() 