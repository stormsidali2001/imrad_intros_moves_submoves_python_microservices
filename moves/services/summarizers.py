from .models.summarizer import summarize_introduction
from .models.class_based_summarizer import summarize_sentences_with_classes
from .schemas.class_based_summarizer_schemas import SentenceClass
from services.mappers import map_move, map_sub_move
from typing import List
import json


def summarize_imrad_introduction(introduction: str):
    try:
        return summarize_introduction(introduction)
    except Exception as e:
        print(e.__str__())
        raise e


def summarize_imrad_sentences_with_classes(sentences: List[SentenceClass]):
    try:
        sentences_json = json.dumps(
            [
                {
                    "sentence": s.sentence,
                    "move": map_move(s.move),
                    "subMove": map_sub_move(s.move, s.subMove),
                }
                for s in sentences
            ]
        )
        print("-------------------------")
        print(sentences_json)
        return summarize_sentences_with_classes(sentences_json)
    except Exception as e:
        print(e.__str__())
        raise e
