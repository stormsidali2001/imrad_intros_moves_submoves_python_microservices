---
library_name: tf-keras
pipeline_tag: text-classification
widget:
- text: "This study aims to investigate the impact of social media on political polarization."
  output:
  - label: Outline your purpose(s) and state the nature of your research
    score: 0.92
  - label: State your hypothesis or research question you seek to answer
    score: 0.03
  - label: Share your findings
    score: 0.02
  - label: Elaborate on the value of your research
    score: 0.01
  - label: Outline the structure that the research paper will follow
    score: 0.02
- text: "We hypothesize that exposure to diverse viewpoints on social media will reduce polarization."
  output:
  - label: Outline your purpose(s) and state the nature of your research
    score: 0.02
  - label: State your hypothesis or research question you seek to answer
    score: 0.95
  - label: Share your findings
    score: 0.01
  - label: Elaborate on the value of your research
    score: 0.01
  - label: Outline the structure that the research paper will follow
    score: 0.01
- text: "The findings of this study will provide valuable insights for policymakers and social media platform designers."
  output:
  - label: Outline your purpose(s) and state the nature of your research
    score: 0.02
  - label: State your hypothesis or research question you seek to answer
    score: 0.03
  - label: Share your findings
    score: 0.10
  - label: Elaborate on the value of your research
    score: 0.83
  - label: Outline the structure that the research paper will follow
    score: 0.02
- text: "This paper is structured as follows:..."
  output:
  - label: Outline your purpose(s) and state the nature of your research
    score: 0.01
  - label: State your hypothesis or research question you seek to answer
    score: 0.02
  - label: Share your findings
    score: 0.02
  - label: Elaborate on the value of your research
    score: 0.02
  - label: Outline the structure that the research paper will follow
    score: 0.93
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

## IMRaD Introduction Move 2 Sub-move Classifier

This model is a fine-tuned BERT model that classifies sentences from the "Occupying the Niche" (Move 2) section of scientific research paper introductions into their corresponding sub-moves:

* **Outline your purpose(s) and state the nature of your research:** Stating the research objectives and approach.
* **State your hypothesis or research question you seek to answer:** Presenting the main research question or hypothesis to be tested. 
* **Share your findings:** Briefly summarizing the main findings of the research (less common in introductions). 
* **Elaborate on the value of your research:** Highlighting the significance and potential impact of the research. 
* **Outline the structure that the research paper will follow:** Describing the organization of the paper (e.g., sections, chapters).

**Parent Classifier:**

This model works together with the main IMRaD Introduction Move Classifier: [https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier](https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier)

First, use the parent classifier to identify sentences belonging to "Occupying the Niche" (Move 2). Then, use this sub-move classifier to categorize the specific function each Move 2 sentence serves.

## Intended Uses & Limitations

**Intended Uses:**

* **Scientific Writing Assistance:**  Help researchers and students analyze and improve the structure of their "Occupying the Niche" section by understanding the specific sub-moves they've used. 
* **Literature Review Analysis:**  Identify how authors state their objectives, hypotheses, and the value of their research in introductions.
* **Educational Tool:** Illustrate the sub-moves used in Move 2 to clearly define the research contribution within the niche.

**Limitations:**

* **Domain Specificity:**  Trained on scientific research papers, so accuracy may be lower on other types of text.
* **Sentence-Level Classification:**  Classifies individual sentences, not the entire Move 2 section as a whole.
* **Ambiguity:**  Some sentences might be challenging to categorize definitively, leading to lower confidence scores.

## Training and Evaluation Data

Trained and evaluated on a subset of the "IMRAD Introduction Sentences Moves & Sub-moves Dataset": [https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset](https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset)

This model uses sentences specifically labeled as Move 2, further categorized into the five sub-moves. 

**Training Details:**

* **Base Model:** `google/bert-base-cased`
* **Implementation:** TensorFlow/Keras
* **Evaluation Metrics:** F1 score and accuracy

## How to Use

```python
from transformers import pipeline

# Parent classifier
move_classifier = pipeline("text-classification", model="stormsidali2001/IMRAD_introduction_moves_classifier")

# Move 2 sub-move classifier
submove_classifier_2 = pipeline("text-classification", model="stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier")

sentence = "The findings of this study have significant implications for the field of [your field]."

move_result = move_classifier(sentence)
move = move_result[0]['label']

if move == "Occupying the Niche":
    submove_result = submove_classifier_2(sentence)
    print(submove_result) 