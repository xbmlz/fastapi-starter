import os
from app import schemas

from app.core.config import settings
from app.crud import crud_user
from app.db import session


def create_all() -> None:
    if not os.path.exists(settings.DB_FILE_PATH):
        session.Base.metadata.create_all(bind=session.engine)
        db = session.SessionLocal()
        user = crud_user.get_user_by_email(db, email="997909544@qq.com")
        if not user:
            user_in = schemas.UserCreate(
                email="997909544@qq.com",
                password="123456",
                is_active=True,
            )
            user = crud_user.create_user(db, user_in)  # noqa: F841
