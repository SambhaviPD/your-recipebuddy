import openai

from .configuration import ResponseModel

def get_recipe_using_openai(api_key, prompt, success_message):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2048
    )
    final_response = ResponseModel(
        success=True, \
        message=success_message, \
        data=response
    )
    return final_response