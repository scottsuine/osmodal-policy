from app import app, db
from models import User
from werkzeug.security import generate_password_hash
import os

def create_admin_user():
    with app.app_context():
        # Check if admin user already exists
        admin = User.query.filter_by(username=os.getenv('ADMIN_USERNAME')).first()
        if not admin:
            admin = User(
                username=os.getenv('ADMIN_USERNAME'),
                password=generate_password_hash(os.getenv('ADMIN_PASSWORD')),
                is_admin=True
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully!")
        else:
            print("Admin user already exists!")

if __name__ == "__main__":
    create_admin_user() 