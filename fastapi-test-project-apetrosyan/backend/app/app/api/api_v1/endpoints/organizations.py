from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Organization])
def read_organizations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve Organizations.
    """
    items = crud.organization.get_multi(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=schemas.Organization)
def create_organization(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.OrganizationCreate
) -> Any:
    """
    Create new organization.
    """
    item = crud.organization.create(db=db, obj_in=item_in)
    return item


@router.patch("/{id}", response_model=schemas.Organization)
def update_organization(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.OrganizationUpdate,
) -> Any:
    """
    Update an organization.
    """
    organization = crud.organization.get(db=db, id=id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    item = crud.organization.update(db=db, db_obj=organization, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.Organization)
def read_organization(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get Organization by ID.
    """
    organization = crud.organization.get(db=db, id=id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.delete("/{id}", response_model=schemas.Organization)
def delete_organization(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete an organization by id.
    """
    organization = crud.organization.get(db=db, id=id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    organization_db = crud.organization.remove(db=db, id=id)
    return organization_db
