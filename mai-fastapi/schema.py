import datetime

from pydantic import BaseModel


class PydancticModel(BaseModel):
    class Config:
        orm_mode = True


class LegalEntityBase(PydancticModel):
    email: str
    phone: str | None


class LegalEntityCreate(LegalEntityBase):
    address_id: int


class AddressBase(PydancticModel):
    street: str
    zip_code: str
    city: str | None
    state: str | None
    country: str


class AddressCreate(AddressBase):
    pass


class ContactCreate(LegalEntityBase):
    address: AddressCreate


class PersonBase(PydancticModel):
    first_name: str
    last_name: str | None


class PersonCreate(PersonBase):
    contact: ContactCreate


class Person(PersonBase):
    id: int


class CompanyBase(PydancticModel):
    name: str
    website: str | None
    registration_number: str | None


class CompanyCreate(CompanyBase):
    contact: ContactCreate


class UserBase(PydancticModel):
    email: str


class UserCreate(UserBase):
    password: str


class InvoiceBase(PydancticModel):
    number: str
    created_at: datetime.date = datetime.date.today()


class InvoiceLineItemBase(PydancticModel):
    pass
