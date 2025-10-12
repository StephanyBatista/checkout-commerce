from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.checkout.checkout_model import Checkout, CheckoutStatus
from app.checkout.checkout_request import CheckoutRequest
from app.infra.database import get_db


async def checkout_process(
    checkout_request: CheckoutRequest, db: AsyncSession = Depends(get_db)
):
    checkout = Checkout(
        customer_email=checkout_request.customer_email,
        total_amount=sum(item.price for item in checkout_request.items),
        status=CheckoutStatus.PENDING.value,
    )
    db.add(checkout)
    await db.commit()
    await db.refresh(checkout)
