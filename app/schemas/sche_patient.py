from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import SexChoices


class PatientBase(BaseModel):
    class Config:
        orm_mode = True


class PatientItemResponse(PatientBase):
    id: int
    identification_number: str
    name: str
    sex: SexChoices
    birthday: Optional[datetime]
    insurance_number: Optional[str]
    email: Optional[EmailStr]


class PatientCreateRequest(PatientBase):
    identification_number: str
    name: str
    sex: SexChoices
    birthday: Optional[datetime]
    insurance_number: Optional[str]
    email: Optional[EmailStr]


class PatientUpdateRequest(BaseModel):
    identification_number: Optional[str]
    name: Optional[str]
    sex: Optional[SexChoices]
    birthday: Optional[datetime]
    insurance_number: Optional[str]
    email: Optional[EmailStr]


class PatientDeleteRequest(BaseModel):
    pass
