import openai
from random import random

openai.api_key = "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"


def get_openAI(prompt: str):
    try:
        model_engine = "text-davinci-003"
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=random(),
        )
        return completion.choices[0].text.strip()
    except:
        return None
