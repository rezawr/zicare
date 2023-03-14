from sqlalchemy import Column, String, Enum, Date

from app.models.model_base import BareBaseModel
from app.helpers.enums import SexChoices


class Patient(BareBaseModel):
    identification_number = Column(String(255), unique=True, index=True)
    name = Column(String(255), index=True)
    sex = Column(Enum(SexChoices))
    birthday = Column(Date)
    insurance_number = Column(String(100), nullable=True)
    email = Column(String(255), nullable=True)

    def __repr__(self):
        return self.name
