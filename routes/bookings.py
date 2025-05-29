from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from middlewares.validate import validate_with_schema
from middlewares.auth_middleware import token_required
from schemas import BookingSchema
from controllers.booking_controller import get_user_bookings, get_booking_by_id, create_booking, cancel_booking
from utils.errors import NotFoundError, BadRequestError

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/', methods=['GET'])
@token_required
def get_bookings():
    db = SessionLocal()
    try:
        bookings = get_user_bookings(db, request.user['id'])
        return jsonify({"success": True, "bookings": bookings}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@bookings_bp.route('/<booking_id>', methods=['GET'])
@token_required
def get_booking(booking_id):
    db = SessionLocal()
    try:
        booking = get_booking_by_id(db, booking_id, request.user['id'])
        return jsonify({"success": True, "booking": booking}), 200
    except NotFoundError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@bookings_bp.route('/', methods=['POST'])
@token_required
@validate_with_schema(BookingSchema)
def create_booking_route():
    data = request.validated_data
    db = SessionLocal()
    try:
        booking = create_booking(db, data['trainId'], request.user['id'])
        return jsonify({
            "success": True,
            "bookingId": booking.id,
            "message": "Seat booked successfully"
        }), 201
    except (NotFoundError, BadRequestError) as e:
        db.rollback()
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@bookings_bp.route('/<booking_id>', methods=['DELETE'])
@token_required
def cancel_booking_route(booking_id):
    db = SessionLocal()
    try:
        cancel_booking(db, booking_id, request.user['id'])
        return jsonify({"success": True, "message": "Booking cancelled successfully"}), 200
    except NotFoundError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close() 