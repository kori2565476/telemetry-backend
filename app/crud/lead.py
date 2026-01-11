from sqlmodel import Session, select

from app.models.lead import Lead
from app.schemas.lead import LeadCreate


def create_lead(session: Session, lead_in: LeadCreate) -> Lead:
    lead = Lead.model_validate(lead_in)
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead


def get_leads(session: Session) -> list[Lead]:
    return session.exec(select(Lead)).all()


def qualify_lead(session: Session, lead: Lead) -> Lead:
    lead.status = "qualified"
    session.add(lead)
    session.commit()
    session.refresh(lead)
    return lead
