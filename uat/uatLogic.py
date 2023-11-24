import openai
import os
import prompt
import json
import time
from concurrent.futures import *
import traceback

class UATLogic:
    def __init__(self):
        api_key = os.getenv('OPENAI_KEY')
        openai.api_key = api_key
    
    def generateUAT(self, useCase):
        start = time.time()
        count = 0
        timeout = 4
        while True:
            try:
                response = openai.ChatCompletion.create(model='gpt-4-1106-preview',
                                messages=[{"role": "system", "content": prompt.SYSTEM_LIST_TESTS},
                                        {"role": "user", "content": useCase}],
                                max_tokens=2000,
                                temperature = 0,
                                request_timeout=480)
                # Response from gpt
                res = response.choices[0].message.content
                # Converting the response into JSON
                i = res.find("```json")
                if i != -1:
                    res = res[7:len(res)-3]
                uat_list = json.loads(res)
                break
            except Exception as e:
                print(traceback.format_exc())
                time.sleep(timeout)
                timeout = timeout *2
                count = count+1

        uats = []
        executor = ThreadPoolExecutor(4)
        futures = []
        for i in uat_list["TESTS"]:
            id = i["ID"]
            descr = i["DESCRIZIONE"]
            uc = i["UC"]
            trivial = i["SS"]
            if trivial.lower() != "s" and i["ES"].lower() != "n":
                futures.append(executor.submit(self.generateUATByID, useCase, res, id, descr, uc))

        for future in as_completed(futures):
            result = future.result()
            uats.append(result)

        uats = sorted(uats, key=lambda d: d['ID']) 

        # Loop over the TESTS provided by GPT
        #for i in uat_list["TESTS"]:
        #    id = i["ID"]
        #    descr = i["DESCRIZIONE"]
        #    uc = i["UC"]
        #    trivial = i["SS"]
        #    if trivial.lower() != "s":
        #        # UAT generation
        #        uat_list = self.generateUATByID(useCase, res, id, descr, uc)
        #        uats.append(uat_list)
        
        end = time.time()
        print("DURATA", end-start)
        return uats
    
    def generateUATByID(self, useCase, output, id, descr, ucid):
        # UAT generation
        count = 0
        timeout = 4
        while True:
            try:
                print(prompt.USER_PRODUCE_UAT.format(UC=useCase, output1=output, ID_UAT=id))
                response = openai.ChatCompletion.create(model='gpt-4-1106-preview',
                                    messages=[{"role": "system", "content": prompt.SYSTEM_PRODUCE_UAT},
                                            {"role": "user", "content": prompt.USER_PRODUCE_UAT.format(UC=useCase, output1=output, ID_UAT=id)}],
                                    max_tokens=2000,
                                    temperature = 0,
                                    request_timeout=480)
                res = response.choices[0].message.content
                j = res.find("```json")
                if j != -1:
                    res = res[7:len(res)-3]
                print(res)
                uat_list = json.loads(res)
                uat_list["ID"] = id
                uat_list["DESCRIZIONE"] = descr
                uat_list["UC"] = ucid
                return uat_list
            except Exception as e:
                print(traceback.format_exc())
                time.sleep(timeout)
                timeout = timeout *2
                count = count+1