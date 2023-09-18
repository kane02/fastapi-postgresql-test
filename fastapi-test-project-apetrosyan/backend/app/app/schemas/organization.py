from typing import Optional

from pydantic import BaseModel


# Shared properties
class OrganizationBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class OrganizationCreate(OrganizationBase):
    name: str
    description: str


# Properties to receive on item update
class OrganizationUpdate(OrganizationBase):
    pass


# Properties shared by models stored in DB
class OrganizationInDBBase(OrganizationBase):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


# Properties to return to client
class Organization(OrganizationInDBBase):
    pass


# Properties stored in DB
class OrganizationInDB(OrganizationInDBBase):
    pass
