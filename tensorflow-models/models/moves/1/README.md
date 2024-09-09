---
library_name: tf-keras
pipeline_tag: text-classification
widget:
- text: Electronic cigarettes (also known as vapes, vaporizers, or vape pens) were introduced into the US market in 2007.
  output:
  - label: Establishing a Research Territory
    score: 0.9
  - label: Establishing a Niche
    score: 0.05
  - label: Occupying the Niche
    score: 0.05
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

## IMRaD Introduction Move Classifier

This model is a fine-tuned BERT model designed to classify sentences from the introductions of scientific research papers into one of three IMRaD moves:

* **Establishing a Research Territory:** Setting the context and background information for the research.
* **Establishing a Niche:** Identifying a gap or problem in existing research.
* **Occupying the Niche:** Proposing a solution or approach to address the identified gap.

## Intended Uses & Limitations

**Intended Uses:**

* **Scientific Writing Assistance:** Help researchers and students analyze and improve the structure of their introductions by identifying the IMRaD moves present in each sentence.
* **Literature Review Analysis:**  Assist in quickly understanding the rhetorical structure of introductions in a set of research papers.
* **Educational Tool:** Illustrate IMRaD concepts and their practical application in scientific writing. 

**Limitations:**

* **Domain Specificity:** The model was trained on a dataset of scientific research papers and might not perform as well on other types of text.
* **Accuracy:** While the model achieves good accuracy, it's not perfect. Predictions should be reviewed carefully, especially in complex or ambiguous sentences.
* **Sentence-Level Classification:**  The model classifies individual sentences. It does not provide an overall analysis of the entire introduction.

## Training and Evaluation Data

The model was trained and evaluated on the "IMRAD Introduction Sentences Moves & Sub-moves Dataset" available on Hugging Face: [https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset](https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset)

The dataset consists of sentences extracted from scientific research paper introductions, manually labeled with their corresponding IMRaD moves.

**Training Details:**

* The `bert-base-cased` model from Google was used as the base model.
* Fine-tuning was performed using a TensorFlow/Keras implementation. 
* Evaluation metrics include F1 score and accuracy.

## How to Use

You can use this model with the `pipeline` function from the `transformers` library:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="your-username/your-model-name")

sentence = "Electronic cigarettes were introduced into the US market in 2007."
result = classifier(sentence)

print(result)