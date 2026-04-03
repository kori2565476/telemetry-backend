from sqlmodel import SQLModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class DeviceCreate(SQLModel):
    name: str
    serial_number: str
    company: Optional[str] = None


class DeviceRead(SQLModel):
    id: UUID
    name: str
    serial_number: str
    company: Optional[str]
    status: str
    created_at: datetime
    last_seen: Optional[datetime]


class DeviceWithKeyResponse(DeviceRead):
    api_key: str