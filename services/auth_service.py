from models import User

def find_user_by_email(db, email):
    return db.query(User).filter(User.email == email).first()

def create_user(db, email, hashed_password):
    user = User(
        email=email,
        password=hashed_password
    )
    db.add(user)
    db.commit()
    return user 