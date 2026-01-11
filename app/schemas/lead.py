from sqlmodel import SQLModel


class LeadCreate(SQLModel):
    email: str
    name: str | None = None
    company: str | None = None
    source: str
    industry: str | None = None


class LeadRead(SQLModel):
    id: int
    email: str
    name: str | None
    company: str | None
    source: str
    industry: str | None
    status: str
