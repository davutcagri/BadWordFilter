from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def checkMessage(message):
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=os.getenv("ASSISTANT_ID")
    )

    if run.status == "completed":
        responses = client.beta.threads.messages.list(thread_id=thread.id)
        return extractFirstContentText(responses)
    else:
        return message

def extractFirstContentText(responses):
    if responses.data and len(responses.data[0].content) > 0:
        return responses.data[0].content[0].text.value
    return None