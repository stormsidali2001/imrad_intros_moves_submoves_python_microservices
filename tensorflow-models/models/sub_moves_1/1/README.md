---
library_name: tf-keras
pipeline_tag: text-classification
widget:
- text: "However, existing research has primarily focused on urban environments, neglecting the unique challenges faced in rural areas."
  output:
  - label: Claim something is wrong with the previous research
    score: 0.1
  - label: Highlight a gap in the field
    score: 0.85
  - label: Raise a question where research in the field is unclear
    score: 0.03
  - label: Extend prior research to add more information on the topic
    score: 0.02
- text: "Previous studies have failed to adequately address the long-term effects of this intervention."
  output:
  - label: Claim something is wrong with the previous research
    score: 0.9
  - label: Highlight a gap in the field
    score: 0.05
  - label: Raise a question where research in the field is unclear
    score: 0.03
  - label: Extend prior research to add more information on the topic
    score: 0.02
- text: "It is therefore crucial to investigate the effectiveness of [your approach] in a rural context."
  output:
  - label: Claim something is wrong with the previous research
    score: 0.05
  - label: Highlight a gap in the field
    score: 0.15
  - label: Raise a question where research in the field is unclear
    score: 0.1
  - label: Extend prior research to add more information on the topic
    score: 0.7
license: mit
datasets:
- stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset
language:
- en
metrics:
- f1
- accuracy
base_model: google/bert-base-cased
---

## IMRaD Introduction Move 1 Sub-move Classifier

This model is a fine-tuned BERT model that classifies sentences from the "Establishing a Niche" (Move 1) section of scientific research paper introductions into their corresponding sub-moves:

* **Claim something is wrong with the previous research:**  Pointing out limitations, flaws, or areas where past research falls short.
* **Highlight a gap in the field:** Identifying areas where knowledge or research is lacking.
* **Raise a question where research in the field is unclear:** Presenting an unanswered question or ambiguity in existing research. 
* **Extend prior research to add more information on the topic:** Suggesting a new direction or contribution building on previous work.

**Parent Classifier:**

This model works in tandem with the main IMRaD Introduction Move Classifier: [https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier](https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier)

First, use the parent classifier to identify sentences belonging to "Establishing a Niche" (Move 1). Then, utilize this sub-move classifier to analyze the specific role each Move 1 sentence plays in establishing the research niche.

## Intended Uses & Limitations

**Intended Uses:**

* **Scientific Writing Assistance:** Help researchers and students analyze and strengthen their "Establishing a Niche" section by precisely categorizing each sentence's sub-move. 
* **Literature Review Analysis:**  Gain a deeper understanding of how authors establish the need for their research by identifying the specific sub-moves used in Move 1.
* **Educational Tool:**  Demonstrate the various sub-moves employed to establish a research niche in scientific writing.

**Limitations:**

* **Domain Specificity:**  Trained on scientific research papers; accuracy may vary on other text types.
* **Sentence-Level Classification:**  Focuses on individual sentences; does not provide a holistic analysis of the entire Move 1 section.
* **Prediction Accuracy:**  While generally accurate, the model might misclassify complex or ambiguous sentences. Review predictions critically.

## Training and Evaluation Data

Trained and evaluated on a subset of the "IMRAD Introduction Sentences Moves & Sub-moves Dataset": [https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset](https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset)

Specifically, the model uses sentences labeled as Move 1, further classified into the four sub-moves. 

**Training Details:**

* **Base Model:**  `google/bert-base-cased`
* **Implementation:** TensorFlow/Keras
* **Evaluation Metrics:** F1 score and accuracy 

## How to Use

```python
from transformers import pipeline

# Parent classifier
move_classifier = pipeline("text-classification", model="stormsidali2001/IMRAD_introduction_moves_classifier")

# Move 1 sub-move classifier
submove_classifier_1 = pipeline("text-classification", model="stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier")

sentence = "This gap in research highlights the need for further investigation into [topic]." 

move_result = move_classifier(sentence)
move = move_result[0]['label']

if move == "Establishing a Niche":
    submove_result = submove_classifier_1(sentence)
    print(submove_result)