from services.train_service import (
    find_trains_by_route,
    find_train_by_id,
    create_train as create_train_service,
    find_all_trains
)
from utils.errors import NotFoundError

def get_available_trains(db, source=None, destination=None):
    if source and destination:
        trains = find_trains_by_route(db, source, destination)
    else:
        trains = find_all_trains(db)
    
    return [{
        'id': train.Train.id,
        'name': train.Train.name,
        'source': train.Train.source,
        'destination': train.Train.destination,
        'totalSeats': train.Train.total_seats,
        'availableSeats': train.available_seats
    } for train in trains]

def get_train_by_id(db, train_id):
    train = find_train_by_id(db, train_id)
    
    if not train:
        raise NotFoundError("Train not found")
        
    return {
        'id': train.id,
        'name': train.name,
        'source': train.source,
        'destination': train.destination,
        'totalSeats': train.total_seats
    }

def create_train(db, train_data):
    return create_train_service(db, train_data) 