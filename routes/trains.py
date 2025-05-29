from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from middlewares.validate import validate_with_schema
from schemas import TrainSchema
from controllers.train_controller import get_available_trains, get_train_by_id, create_train
from utils.errors import NotFoundError

trains_bp = Blueprint('trains', __name__)

@trains_bp.route('/', methods=['GET'])
def get_trains():
    db = SessionLocal()
    try:
        source = request.args.get('source')
        destination = request.args.get('destination')
        trains = get_available_trains(db, source, destination)
        return jsonify({"success": True, "trains": trains}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@trains_bp.route('/<train_id>', methods=['GET'])
def get_train(train_id):
    db = SessionLocal()
    try:
        train = get_train_by_id(db, train_id)
        return jsonify({"success": True, "train": train}), 200
    except NotFoundError as e:
        return jsonify({"error": str(e)}), e.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@trains_bp.route('/', methods=['POST'])
@validate_with_schema(TrainSchema)
def create_train_route():
    data = request.validated_data
    db = SessionLocal()
    try:
        train = create_train(db, data)
        return jsonify({"success": True, "message": "Train added"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close() 