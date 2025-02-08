# 🚀 Project Setup Guide

This project is designed to provide a safe and efficient environment by leveraging OpenAI's API for filtering profanity and hate speech. Follow the steps below to set up and run the application smoothly.

## 📌 Installing Required Libraries

To install all necessary dependencies, run the following command:

```sh
pip install -r requirements.txt
```

## 🔑 Setting Up API Credentials

Make sure to configure your API credentials in the `assistant.py` file:

- `OPENAI_API_KEY`
- `ASSISTANT_ID`

## 📡 Example POST Request

You can test the API with the following example request:

### 🌍 Endpoint:

```
http://127.0.0.1:5001/check
```

### 📄 Headers:

```json
Content-Type: application/json
```

### 📩 Request Body:

```json
{
  "messages": [
    "example message 1",
    "example message 2"
  ]
}
```
