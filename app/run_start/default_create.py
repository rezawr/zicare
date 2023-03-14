#import faker.providers
from app.helpers.enums import UserRole
from app.models.model_user import User
from fastapi_sqlalchemy import db
from app.core.security import get_password_hash

#fake = faker.Faker()


class DefaultUser:
    def user(data={}): 
        user = User(
            full_name=data.get('full_name'),
            email=data.get('email'),
            hashed_password=get_password_hash(data.get('password')),
            is_active=data.get('is_active') if data.get('is_active') is not None else True,
            role=data.get('role') if data.get('role') is not None else UserRole.GUEST.value
        )

        """
        | -------------------------------------------------------------------------------
        | FastAPI doesnt have any custom command line, so I used to checking the admin
        | user is there or not, if there admin user is exist it will be going to exception
        | and the exception doesnt have any code to run, and the application could be run
        | properly
        | 
        | *R
        | -------------------------------------------------------------------------------
        """
        try:
            with db():
                db.session.add(user)
                db.session.commit()
                db.session.refresh(user)
            print ("insert first user")
        except Exception as e:
            pass