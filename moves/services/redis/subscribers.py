from services.schemas.summarizer_schemas import (
    GlobalSummaryEventDto,
)
from services.schemas.class_based_summarizer_schemas import (
    ClassBasedSummaryEventDto,
    ClassBasedSummaryCreatedEventDto,
)

from services.summarizers import (
    summarize_imrad_introduction,
    summarize_imrad_sentences_with_classes,
)
from .publishers import (
    publish_global_summary_creation,
    publish_class_based_summary_creation,
)

from .channels import REQUEST_CLASS_BASED_SUMMARY, REQUEST_GLOBAL_SUMMARY
from .client import redis_client


async def init_global_summary_creation_subscriber():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(REQUEST_GLOBAL_SUMMARY)
    async for message in pubsub.listen():
        print("------------------------------")
        print(
            "------------received pubsub data REQUEST_GLOBAL_SUMMARY ------------------"
        )
        if message["type"] == "message":
            try:
                print("-----raw message----")
                print(message)
                print("-----x-raw message----")
                global_summary = GlobalSummaryEventDto.parse_raw(message["data"])
                print(f" summarizing {global_summary}")
                summary = summarize_imrad_introduction(global_summary.content)
                print("---summary---")
                print(summary)
                print("---x-summary---")
                global_summary.content = summary.content

                await publish_global_summary_creation(global_summary)

            except Exception as e:
                print(e.__str__())
                raise e


async def init_class_based_summary_creation_subscriber():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(REQUEST_CLASS_BASED_SUMMARY)
    async for message in pubsub.listen():
        print("------------------------------")
        print(
            "------------received pubsub data REQUEST_CLASS_BASED_SUMMARY ------------------"
        )
        if message["type"] == "message":
            try:
                print("-----raw message----")
                print(message)
                print("-----x-raw message----")
                event = ClassBasedSummaryEventDto.parse_raw(message["data"])
                print(f" summarizing {event}")
                summary = summarize_imrad_sentences_with_classes(event.content)
                print("---summary---")
                print(summary)
                print("---x-summary---")
                outputEvent = ClassBasedSummaryCreatedEventDto(
                    introductionId=event.introductionId,
                    content=summary.class_based_summary,
                )

                await publish_class_based_summary_creation(outputEvent)

            except Exception as e:
                print(e.__str__())
                raise e
