from datetime import datetime
from sqlmodel import SQLModel, Field


class Lead(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    email: str = Field(index=True)
    name: str | None = None
    company: str | None = None

    source: str  # LinkedIn, Web, Referido
    industry: str | None = None

    status: str = Field(default="new", index=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)
