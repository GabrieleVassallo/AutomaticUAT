import openai
import os
import prompt
import json

class UATLogic:
    def __init__(self):
        api_key = os.getenv('OPENAI_KEY')
        openai.api_key = api_key
    
    def generateUAT(self, useCase):
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',
                        messages=[{"role": "system", "content": prompt.SYSTEM_LIST_TESTS},
                                  {"role": "user", "content": useCase}],
                        max_tokens=2000,
                        temperature = 0)
        # Response from gpt
        res = response.choices[0].message.content
        # Converting the response into JSON
        uat_list = json.loads(res)
        uats = []

        # Loop over the TESTS provided by GPT
        for i in uat_list["TESTS"]:
            id = i["ID"]
            descr = i["DESCRIPTION"]
            uc = i["UC"]
            input = f"""ID USE CASE {uc}
            ID TEST: {id}
            TEST DESCRIPTION: {descr}
            """
            # UAT generation
            response = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k',
                        messages=[{"role": "system", "content": prompt.SYSTEM_PRODUCE_UAT},
                                  {"role": "user", "content": input}],
                        max_tokens=2000,
                        temperature = 0)
            res = response.choices[0].message.content
            uat_list = json.loads(res)
            uats.append(uat_list)
        return uats
    