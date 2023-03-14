import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse, ResponseSchemaBase
from app.schemas.sche_patient import PatientItemResponse, PatientCreateRequest, PatientUpdateRequest, PatientDeleteRequest
from app.services.srv_patient import PatientService
from app.models.model_patient import Patient

logger = logging.getLogger()
router = APIRouter()


@router.get("", dependencies=[Depends(login_required)], response_model=Page[PatientItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Patient
    """
    try:
        _query = db.session.query(Patient)
        patients = paginate(model=Patient, query=_query, params=params)
        return patients
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[PatientItemResponse])
def create(form_data: PatientCreateRequest) -> Any:
    """
    API Create Patient
    """
    try:
        exist_patient = db.session.query(Patient).filter(Patient.identification_number == form_data.identification_number).first()

        if exist_patient:
            raise Exception('Identification Number already exists')

        if form_data.email is not None:
            exist_email = db.session.query(Patient).filter(Patient.email == form_data.email).first()
            if exist_email:
                raise Exception('Email already exists')

        if form_data.insurance_number is not None:
            exist_insurance = db.session.query(Patient).filter(Patient.insurance_number == form_data.insurance_number).first()
            if exist_insurance:
                raise Exception('Insurance already exists')

        patient = PatientService().create(form_data)
        return DataResponse().success_response(data=patient)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/{patient_id}", dependencies=[Depends(login_required)], response_model=DataResponse[PatientItemResponse])
def detail(patient_id: int) -> Any:
    """
    API get Detail Patient
    """
    try:
        exist_patient = db.session.query(Patient).get(patient_id)
        if exist_patient is None:
            raise Exception('Patient not exists')

        return DataResponse().success_response(data=exist_patient)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.put("/{patient_id}", dependencies=[Depends(PermissionRequired('administrators'))],
            response_model=DataResponse[PatientItemResponse])
def update(patient_id: int, form_data: PatientUpdateRequest) -> Any:
    """
    API update Patient
    """
    try:
        exist_patient = db.session.query(Patient).get(patient_id)
        if exist_patient is None:
            raise Exception('Patient not exists')

        updated_user = PatientService().update(patient=exist_patient, data=form_data)
        return DataResponse().success_response(data=updated_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.delete("/{patient_id}", dependencies=[Depends(PermissionRequired('administrators'))],
            response_model=DataResponse[PatientDeleteRequest])
def delete(patient_id: int) -> Any:
    """
    API Delete Patient
    """
    try:
        patient = db.session.query(Patient).get(patient_id)
        if patient is None:
            raise Exception('Patient not exists')

        db.session.delete(patient)
        db.session.commit()

        return ResponseSchemaBase().custom_response(000, f"Patient {patient_id} deleted")
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
