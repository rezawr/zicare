import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_patient import Patient
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_patient import PatientCreateRequest, PatientUpdateRequest



class PatientService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create(data: PatientCreateRequest):
        patient = Patient(
            identification_number=data.identification_number,
            name=data.name,
            sex=data.sex,
            birthday=data.birthday,
            insurance_number=data.insurance_number,
            email=data.email
        )
        db.session.add(patient)
        db.session.commit()
        return patient

    @staticmethod
    def update(patient: Patient, data: PatientUpdateRequest):
        patient.identification_number = patient.identification_number if data.identification_number is None else data.identification_number
        patient.name = patient.name if data.name is None else data.name
        patient.sex = patient.sex if data.sex is None else data.sex
        patient.birthday = patient.birthday if data.birthday is None else data.birthday
        patient.insurance_number = patient.insurance_number if data.insurance_number is None else data.insurance_number
        patient.email = patient.email if data.email is None else data.email

        identification_number = db.session.query(Patient).filter(
            (Patient.identification_number == patient.identification_number) &
            (Patient.id != patient.id)
        ).first()

        if identification_number:
            raise Exception("Identification number already exist")
        
        if patient.insurance_number is not None:
            insurance_exists = db.session.query(Patient).filter(
                (Patient.insurance_number == patient.insurance_number) &
                (Patient.id != patient.id)
            ).first()

            if insurance_exists:
                raise Exception("Insurance number already exists")

        if patient.email is not None:
            email_exists = db.session.query(Patient).filter(
                (Patient.email == patient.email) &
                (Patient.id != patient.id)
            ).first()

            if email_exists:
                raise Exception("Email already exists")

        db.session.commit()

        return patient
