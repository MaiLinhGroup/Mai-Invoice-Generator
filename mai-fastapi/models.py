import datetime
import decimal
import enum
from typing import List

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Currency(enum.Enum):
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    CHF = "CHF"
    JPY = "JPY"
    AUD = "AUD"
    CAD = "CAD"
    CZK = "CZK"
    PLN = "PLN"


class QuantityUnit(enum.Enum):
    i = "item(s)"
    d = "day(s)"
    h = "hour(s)"


class LegalEntity(Base):
    __tablename__ = "legal_entities"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone: Mapped[str | None]
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"), index=True)

    address: Mapped["Address"] = relationship(back_populates="legal_entities")
    person: Mapped["Person"] = relationship(back_populates="legal_entity")
    company: Mapped["Company"] = relationship(back_populates="legal_entity")

    invoices: Mapped[List["Invoice"]] = relationship(
        foreign_keys="Invoice.owner_id", back_populates="owner"
    )
    bills: Mapped[List["Invoice"]] = relationship(
        foreign_keys="Invoice.bill_to_id", back_populates="bill_to"
    )


class Person(Base):
    __tablename__ = "people"
    __table_args__ = UniqueConstraint(
        "legal_entity_id",
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(index=True)
    last_name: Mapped[str | None]
    legal_entity_id: Mapped[int] = mapped_column(
        ForeignKey("legal_entities.id"),
        index=True,
    )

    legal_entity: Mapped["LegalEntity"] = relationship(
        back_populates="person", single_parent=True
    )


class Company(Base):
    __tablename__ = "companies"
    __table_args__ = UniqueConstraint(
        "legal_entity_id",
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True)
    registration_number: Mapped[str | None] = mapped_column(unique=True)
    legal_entity_id: Mapped[int] = mapped_column(
        ForeignKey("legal_entities.id"),
        index=True,
    )

    legal_entity: Mapped["LegalEntity"] = relationship(
        back_populates="company", single_parent=True
    )


class Address(Base):
    __tablename__ = "addresses"
    __table_args__ = UniqueConstraint("street", "zip_code")

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str]
    zip_code: Mapped[str]
    city: Mapped[str | None]
    state: Mapped[str | None]
    country: Mapped[str] = mapped_column(index=True)

    legal_entities: Mapped[List["LegalEntity"]] = relationship(back_populates="address")


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime.date] = mapped_column(index=True)
    vat_percentage: Mapped[int]
    vat_amount: Mapped[decimal.Decimal]
    total_amount_net: Mapped[decimal.Decimal]
    total_amount_gross: Mapped[decimal.Decimal]
    currency: Mapped[Currency]
    owner_id: Mapped[int] = mapped_column(ForeignKey("legal_entities.id"), index=True)
    bill_to_id: Mapped[int] = mapped_column(ForeignKey("legal_entities.id"))

    owner: Mapped["LegalEntity"] = relationship(back_populates="invoices")
    bill_to: Mapped["LegalEntity"] = relationship(back_populates="bills")

    line_items: Mapped[List["InvoiceLineItem"]] = relationship(back_populates="invoice")


class InvoiceLineItem(Base):
    __tablename__ = "invoice_line_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    quantity: Mapped[decimal.Decimal]
    quantity_unit: Mapped[QuantityUnit]
    unit_price: Mapped[decimal.Decimal]
    total_price: Mapped[decimal.Decimal]
    currency: Mapped[Currency]
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), index=True)
    invoice_number: Mapped[str] = mapped_column(
        ForeignKey("invoices.number"), index=True
    )

    invoice: Mapped["Invoice"] = relationship(back_populates="line_items")
