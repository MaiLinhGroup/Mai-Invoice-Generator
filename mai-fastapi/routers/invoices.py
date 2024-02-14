# Path: mai-fastapi/routers/invoices.py
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"],
    responses={404: {"description": "Not found"}},
)
fake_invoice_db = [
    {"INV-ID": id, "Description": f"INV-{id}"} for id in range(1, 6)
]  # noqa: E501


@router.get("/", summary="Get all invoices")
async def read_invoices():
    return fake_invoice_db


@router.get("/{id}", summary="Get invoice by id")
async def read_invoice(id: int):
    for invoice in fake_invoice_db:
        if invoice.get("INV-ID") == id:
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")


@router.post("/", summary="Create invoice")
async def create_invoice():
    return {"message": "Invoice has been created successfully."}


@router.get(
    "/{id}/pdf",
    summary="Get PDF version of invoice",
    description="This will return the PDF version of the invoice.",
)
async def create_invoice_pdf(id: int):
    return {"message": f"PDF for Invoice {id} has been created successfully."}


@router.put("/{id}", summary="Update invoice by id")
async def update_invoice(id: int):
    return {"message": f"Invoice {id} has been updated successfully."}


@router.delete("/{id}", summary="Delete invoice by id")
async def delete_invoice(id: int):
    return {"message": f"Invoice {id} has been deleted successfully."}


@router.delete("/", summary="Delete all invoices")
async def delete_all_invoices():
    return {"message": "All invoices have been deleted successfully."}
