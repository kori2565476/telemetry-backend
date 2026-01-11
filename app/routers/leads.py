from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.session import get_session
from app.crud.lead import create_lead, get_leads, qualify_lead
from app.schemas.lead import LeadCreate, LeadRead
from app.models.lead import Lead

router = APIRouter(
    prefix="/leads",
    tags=["leads"]
)


@router.post("/", response_model=LeadRead)
def create_lead_endpoint(
    lead_in: LeadCreate,
    session: Session = Depends(get_session),
):
    return create_lead(session, lead_in)


@router.get("/", response_model=list[LeadRead])
def list_leads(
    session: Session = Depends(get_session),
):
    return get_leads(session)

@router.post("/{lead_id}/qualify", response_model=LeadRead)
def qualify_lead_endpoint(
    lead_id: int,
    session: Session = Depends(get_session),
):
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    return qualify_lead(session, lead)
