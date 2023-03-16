from config import chat_config


def code_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/engines/code-davinci-001/completions",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            max_tokens=1024,
            n=3,
            stop=None,
            temperature=0.7
        )
    )
    return response_data


def text_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5
        )
    )
    return response_data


def image_create_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/images/generations",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            response_format="url",
            model="image-alpha-001",
            num_images=3
        )
    )
    return response_data
