# project/app/api/crud.py

from typing import Union

from fastapi import APIRouter

from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import TextSummary

router = APIRouter()


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None
