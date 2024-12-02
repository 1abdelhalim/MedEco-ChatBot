
# MedEco ChatBot

MedEco ChatBot is a healthcare chatbot designed to provide information about drug-drug interactions, drug-food interactions, and medicine alternatives. It is powered by OpenAI's GPT-3 API and is deployed as a web service on Azure.

## Features

- **Drug-Drug Interactions**: Provides information on potential interactions between medications.
- **Drug-Food Interactions**: Explains how different foods can interact with medications.
- **Medicine Alternatives**: Suggests alternative medicines for specific conditions.

## Technologies Used

- **Python**: The backend programming language for the chatbot.
- **FastAPI**: Used to build the RESTful API for the chatbot.
- **OpenAI API**: Provides natural language processing capabilities to interpret queries.
- **Docker**: Containers the application for easy deployment and scalability.
- **Azure**: Hosts the web application and provides a reliable cloud infrastructure.

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/1abdelhalim/MedEco-ChatBot.git
cd MedEco-ChatBot
```

### 2. Set Up a Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Your OpenAI API Key
Set the OpenAI API Key either in your environment variables or directly in the code.

### 5. Run the Application Locally
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
Available at [http://localhost:8000](http://localhost:8000).

## API Usage

Send a `POST` request to `/query` with a JSON body containing your query.


## Deployment

The application is deployed on Azure
