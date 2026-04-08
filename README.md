
# IMRaD Introduction Analysis - AI Models and PDF Extractor Microservices 

This repository contains the backend microservices responsible for the core AI-powered analysis and PDF processing functionality of the IMRaD Introduction Analysis platform. This platform is developed as part of my graduation thesis. 

**Parent Repository (Next.js Frontend & API):**
[https://github.com/stormsidali2001/graduation_IMRAD_introduction_analysis_SaaS](https://github.com/stormsidali2001/graduation_IMRAD_introduction_analysis_SaaS)

## Microservices

This repository hosts two independent microservices:

* **AI Models Microservice (FastAPI):** 
    * Handles interaction with the TensorFlow Serving service to get predictions from the trained AI models. 
    * Provides additional features like summarization and author thought process generation, utilizing the Gemini API.

* **PDF Extractor Microservice (FastAPI):**
    * Extracts the introduction text from research papers uploaded in PDF format. 

## AI Models

The platform leverages four fine-tuned BERT models hosted on Hugging Face:

* **IMRaD Introduction Move Classifier:**  [https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier](https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier) 
* **IMRaD Introduction Move 0 Sub-move Classifier:** [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier)
* **IMRaD Introduction Move 1 Sub-move Classifier:** [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier)
* **IMRaD Introduction Move 2 Sub-move Classifier:**  [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier) 

These models are responsible for classifying sentences in introductions into their respective IMRaD moves and sub-moves.

## Datasets

The AI models were trained on a unique dataset of over 169,000 sentences. This dataset was generated using Google's Gemini Pro model and a custom-designed pipeline applied to a set of randomly selected introductions from the **unarXive IMRaD Classification Dataset (Hugging Face):** [https://huggingface.co/datasets/saier/unarXive_imrad_clf](https://huggingface.co/datasets/saier/unarXive_imrad_clf).

The process of creating the dataset is documented in the `/notebooks/v3` directory of the main (Next.js) repository: [https://github.com/stormsidali2001/graduation_IMRAD_introduction_analysis_SaaS](https://github.com/stormsidali2001/graduation_IMRAD_introduction_analysis_SaaS)

## TensorFlow Serving

TensorFlow Serving is used to efficiently serve the AI models for prediction.  The Docker Compose configuration for TensorFlow Serving is located in this repository, in the directory for the AI Models Microservice. 

## Repository Structure

* `/moves`: Contains the code for the AI Models Microservice (FastAPI).
* `/pdf-extractor`: Contains the code for the PDF Extractor Microservice (FastAPI).
* `/tensorflow-models`:  Contains the Docker Compose configuration for TensorFlow Serving. 

## Dependencies 

* Python 3.13 (recommended)
* FastAPI
* TensorFlow
* Docker

## Running the Microservices

### Prerequisites
1. Ensure you have **Docker** and **Python 3.13** installed.
2. Recreate the virtual environment and install the necessary Python dependencies:
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   pip install -r moves/requirements.txt
   pip install python-multipart
   ```
3. Ensure a **Eureka Server** is running at `http://localhost:8761`.

### 1. Start TensorFlow Serving
The AI models are served using TensorFlow Serving. Navigate to the `tensorflow-models` directory and start the container:

```bash
cd tensorflow-models
docker-compose up -d
```

### 2. Start AI Models Microservice (Moves)
This service handles IMRaD move classification and summarization.

```bash
source .venv/bin/activate
cd moves
uvicorn main:app --reload --port 8000
```
*The service will be available at `http://localhost:8000`.*

### 3. Start PDF Extractor Microservice
This service extracts text from PDF research papers.

```bash
source .venv/bin/activate
cd pdf-extractor
uvicorn main:app --reload --port 8010
```
*The service will be available at `http://localhost:8010`.*
## License

MIT


