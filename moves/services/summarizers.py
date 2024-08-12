from .models.summarizer import summarize_introduction
from .models.class_based_summarizer import summarize_sentences_with_classes
from .schemas.class_based_summarizer_schemas import SentenceClass
from typing import List
import json


def summarize_imrad_introduction(introduction: str):
    try:
        return summarize_introduction(introduction)
    except Exception as e:
        print(e.__str__())


def summarize_imrad_sentences_with_classes(sentences: List[SentenceClass]):
    try:
        sentences_json = json.dumps(
            {"sentence": s.sentence, "move": s.move, "subMove": s.subMove}
            for s in sentences
        )
        return summarize_sentences_with_classes(sentences_json)
    except Exception as e:
        print(e.__str__())
