
# IMRaD Introduction Analysis Platform (Next.js Microservice)

This repository contains the Next.js-based frontend and API for a Micro SaaS platform designed to analyze the introductions of scientific research papers based on the IMRaD (Introduction, Methods, Results, and Discussion) structure.

## Project Overview

The platform uses state-of-the-art AI models to automatically classify sentences in introductions into their corresponding IMRaD moves and sub-moves. It provides:

* **Automated Analysis:**  Accurately identify and categorize sentences within research paper introductions.
* **Visual Feedback:** Highlight sentences and label them with their predicted moves and sub-moves.
* **Premium Features:**  Offer advanced features like summarization and author thought process analysis for paid subscribers. 
* **User-Friendly Interface:**  Provide an easy-to-use web interface for researchers, students, and educators to analyze introductions and improve their scientific writing. 

## Microservice Architecture

The platform is built using a microservice architecture for scalability and maintainability. This repository is the main microservice, responsible for the frontend user interface, user authentication, API endpoints, and orchestration of other microservices.

**Other Microservices:**

* **User Data Microservice:**  [https://github.com/stormsidali2001/imrad_introduction_moves_sub_moves_express_user_data](https://github.com/stormsidali2001/imrad_introduction_moves_sub_moves_express_user_data)
    * Built with Express.js and TypeScript.
    * Stores user data, analyzed introductions, predictions, summaries, and user feedback. 
    * Manages the feedback system. 

* **AI Models and PDF Extractor Microservices:**  [https://github.com/stormsidali2001/imrad_intros_moves_submoves_python_microservices](https://github.com/stormsidali2001/imrad_intros_moves_submoves_python_microservices)
    * **AI Models Microservice:**
        * Built with FastAPI (Python).
        * Handles interaction with the AI models, predictions, summarization, and thought process generation.
    * **PDF Extractor Microservice:**
        * Built with FastAPI (Python).
        * Extracts introductions from PDF research papers. 

**Additional Components:**

* **TensorFlow Serving:** Deployed using Docker, serves the AI models for prediction. (Docker Compose configuration is in the AI Models Microservice repository).
* **Redis:**  Used as a message broker for asynchronous communication between microservices.

## Datasets

The AI models used in this platform are trained and evaluated on the following datasets:

* **IMRAD Introduction Sentences Moves & Sub-moves Dataset:** [https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset](https://huggingface.co/datasets/stormsidali2001/IMRAD-introduction-sentences-moves-sub-moves-dataset)
    * Contains sentences extracted from scientific research paper introductions, labeled with their corresponding IMRaD moves and sub-moves.

* **unarXive IMRaD Classification Dataset (Hugging Face):** [https://huggingface.co/datasets/saier/unarXive_imrad_clf](https://huggingface.co/datasets/saier/unarXive_imrad_clf) 
    * A larger dataset of IMRaD-structured papers used as a basis for creating the training data.

* **IMRAD Classification Dataset (100k Rows):** [https://huggingface.co/datasets/stormsidali2001/IMRAD-sections-clf-gemini-augmented](https://huggingface.co/datasets/stormsidali2001/IMRAD-sections-clf-gemini-augmented) 
    * An augmented dataset used for training and evaluating models.

**Trained Models:**

The trained TensorFlow models are published on Hugging Face:

* **IMRaD Introduction Move Classifier:**  [https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier](https://huggingface.co/stormsidali2001/IMRAD_introduction_moves_classifier) 
* **IMRaD Introduction Move 0 Sub-move Classifier:** [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier)
* **IMRaD Introduction Move 1 Sub-move Classifier:** [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier)
* **IMRaD Introduction Move 2 Sub-move Classifier:**  [https://huggingface.co/stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier](https://huggingface.co/stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier) 

## Repository Structure

* `/api`: Contains the Next.js API server code.
* `/frontend`: Contains the Next.js frontend code.
* `/nginx`:  Includes the Docker Compose configuration and Nginx configuration files for the API Gateway. 
* `/notebooks`: Contains the Jupyter notebooks used for data analysis, model training, and experimentation. 
* `/images`: Contains screenshots of the application interface.

**App Screens:**

* admin_dashboard_page.png
* admin_subscriptions_page.png
* admin_users_page.png
* app_screens_introduction_details_normal_user.png
* app_screens_introduction_details_premium_user.png
* billing_portal_1.png
* billing_portal_2.png
* dashboard_error_page.png
* error_page.png
* feedbacks_state_1.png
* forgot_password_state_1.png
* forgot_password_state_2.png
* generate_state_1.png
* generate_state_2.png
* generate_state_3.png
* generate_state_4_loading.png
* generate_state_5.png
* introductions_page.png
* loading_page.png
* login.png
* reset_password_callback_page_state_1.png
* reset_password_callback_page_state_2.png
* settings_1.png
* settings_2.png
* sign_up_state_1.png
* sign_up_state_2.png
* submit_feedback_dislike.png
* submit_feedback_like.png
* upgrade_plan_screens_1.png
* upgrade_plan_screens_2_stripe_checkout.png
* upgrade_plan_screens_3_premium_user.png
* verify_email_page_1.png
* verify_email_page_2.png


## Getting Started

[Provide instructions on how to set up and run the project locally. Include prerequisites, installation steps, and how to start the different microservices.] 

## Contributing

Contributions are welcome! 

## License 

[Specify your project's license]


**Key Features:**

* **Appealing:** The README uses clear headings, concise descriptions, and links for easy navigation.
* **Complete:**  Includes references to all datasets, trained models, microservice repositories, and important directories. 
* **Informative:** Provides an overview of the project, architecture, and key components.
* **Actionable:**  Includes a "Getting Started" section to guide users on how to run the project. 

Remember to customize the placeholders (like "[Provide instructions...]") with your specific information.  
