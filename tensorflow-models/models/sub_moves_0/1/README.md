---
library_name: tf-keras
pipeline_tag: text-classification
widget:
- text: "Climate change is a pressing global issue with far-reaching consequences for ecosystems and human societies."
  output:
  - label: Show that the research area is important, problematic, or relevant in some way
    score: 0.95
  - label: Introduce and review previous research in the field
    score: 0.05
- text: "Numerous studies have investigated the impact of rising temperatures on marine biodiversity."
  output:
  - label: Show that the research area is important, problematic, or relevant in some way
    score: 0.1
  - label: Introduce and review previous research in the field
    score: 0.9
- text: "Despite its importance, the specific role of ocean currents in mitigating climate change remains poorly understood." 
  output:
  - label: Show that the research area is important, problematic, or relevant in some way 
    score: 0.55 
  - label: Introduce and review previous research in the field 
    score: 0.45
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

## IMRaD Introduction Move 0 Sub-move Classifier

This model is a fine-tuned BERT model specialized in classifying sentences from the "Establishing a Research Territory" (Move 0) section of scientific research paper introductions into their corresponding sub-moves:

* **Show that the research area is important, problematic, or relevant in some way:**  Highlighting the significance, issues, or relevance of the research topic.
* **Introduce and review previous research in the field:**  Presenting a brief overview of existing work and studies related to the topic.

**Parent Classifier:**

This model is designed to be used in conjunction with the main IMRaD Introduction Move Classifier: [https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier](https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier). 

The parent classifier identifies the overall IMRaD move for each sentence. If a sentence is classified as "Establishing a Research Territory" (Move 0), this sub-move classifier can be used to further analyze the specific purpose of that sentence within Move 0. 

## Intended Uses & Limitations

**Intended Uses:**

* **Scientific Writing Assistance:** Help researchers and students understand and refine the structure of their "Establishing a Research Territory" section.
* **Literature Review Analysis:** Quickly identify how authors establish the context and background in research paper introductions.
* **Educational Tool:**  Illustrate the different sub-moves used to establish a research territory in scientific writing.

**Limitations:**

* **Domain Specificity:**  The model was trained on scientific research papers and may not be as accurate on other types of text.
* **Accuracy:** While the model has good performance, it is not perfect. Predictions should be carefully reviewed.
* **Sentence-Level Classification:** The model classifies individual sentences and does not provide an analysis of the entire "Establishing a Research Territory" section as a whole.

## Training and Evaluation Data

This model was trained and evaluated on a subset of the "IMRAD Introduction Sentences Moves & Sub-moves Dataset" available on Hugging Face: [https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset](https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset)

The dataset includes sentences specifically from Move 0 of introductions, labeled with their respective sub-moves.

**Training Details:**

* **Base Model:** `google/bert-base-cased`
* **Implementation:** TensorFlow/Keras
* **Evaluation Metrics:** F1 score and accuracy

## How to Use

```python
from transformers import pipeline

# Load the parent classifier
move_classifier = pipeline("text-classification", model="stormsidali2001/IMRAD_introduction_moves_classifier")

# Load the sub-move classifier for Move 0
submove_classifier_0 = pipeline("text-classification", model="stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier")

sentence = "Electronic cigarettes were introduced into the US market in 2007."

# First, classify the move 
move_result = move_classifier(sentence)
move = move_result[0]['label']

if move == "Establishing a Research Territory":
    # If Move 0, classify the sub-move
    submove_result = submove_classifier_0(sentence)
    print(submove_result)