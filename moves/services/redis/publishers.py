from .client import redis_client
from .channels import GLOBAL_SUMMARY_CREATED, CLASS_BASED_SUMMARY_CREATED

from services.schemas.summarizer_schemas import GlobalSummaryEventDto
from services.schemas.class_based_summarizer_schemas import (
    ClassBasedSummaryCreatedEventDto,
)


async def publish_message(channel: str, message: str):
    await redis_client.publish(channel, message)


async def publish_global_summary_creation(global_summary: GlobalSummaryEventDto):
    serialized = global_summary.model_dump_json()
    await publish_message(GLOBAL_SUMMARY_CREATED, serialized)


async def publish_class_based_summary_creation(event: ClassBasedSummaryCreatedEventDto):
    serialized = event.model_dump_json()
    await publish_message(CLASS_BASED_SUMMARY_CREATED, serialized)
