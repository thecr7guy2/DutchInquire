# DutchInquire: Dutch Document Analyzer

DutchInquire is a Streamlit-powered application designed to analyze Dutch documents and provide insights in English. It uses Google's Gemini Pro Vision model for processing and is deployed on [HuggingFace Spaces](https://huggingface.co/spaces/thecr7guy/DutchInquire).

<img src="logo.png" alt="DutchInquire logo" style="height: 600px; width:700px;">

## Features

- Analyze images of Dutch documents.
- Convert analysis into English responses.
- User-friendly interface for uploading documents and receiving responses.

## Local Setup with Docker

### Prerequisites

- Docker installed on your system.

### Building the Docker Container

**Clone the Repository**: Clone the repository containing the Dockerfile and Python script.
**Build the Docker Image**:
```bash 
docker build -t dutchinquire 
```
This command builds the Docker image with the tag `dutchinquire`.

**Run the Docker Container**:
```bash 
docker run -p 7860:7860 dutchinquire
```
This makes the app available at `http://localhost:7860`.

### Dockerfile Breakdown

- The Dockerfile uses `python:3.10.13-slim` as a base image.
- It installs `pipenv` for dependency management.
- The application is set up in the `/app` directory inside the container.
- The `Pipfile` and `Pipfile.lock` are copied and dependencies are installed.
- The `app.py` file (containing the Streamlit app) is copied into the container.
- The container exposes port 7860.
- The CMD directive specifies how Streamlit should run the app.

## Usage

1. Open your web browser and navigate to `http://localhost:7860`.
2. Upload an image file of a Dutch document.
3. Enter your query in the provided text box.
4. Click "Ask Now" to receive the analysis.

## Deployment on Hugging Face Spaces

- The application is also deployed on [HuggingFace Spaces](https://huggingface.co/spaces/thecr7guy/DutchInquire), providing an easy-to-access web interface for users.


