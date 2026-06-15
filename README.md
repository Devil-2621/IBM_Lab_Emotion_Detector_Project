# Emotion Detector

An AI-based web application that detects emotions (anger, disgust, fear, joy, sadness) from text input using IBM Watson NLP library.

## Features
- Emotion detection from text using Watson NLP
- Web interface built with Flask
- REST API endpoint for programmatic access
- Comprehensive error handling
- Unit tested

## Tech Stack
- Python 3.x
- Flask
- IBM Watson NLP (via REST API)
- pytest

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python server.py
```

Then open `http://localhost:5000` in your browser.

## API Endpoint
```
POST /emotionDetector
Body: {"textToAnalyze": "Your text here"}
```

## Testing
```bash
python -m pytest tests/
```
