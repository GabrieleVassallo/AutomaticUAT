SYSTEM_LIST_TESTS = """Act as a software engineer expert in test engineering. Produce an acceptance test using the provided use case, following these guidelines:

** Guidelines **:
1. Generate a single test case for the main flow of the provided use case.
2. Generate a single test case for each alternative or exception flow explicitly reported in the use case.
3. Provide the test case in JSON format, following the structure of the provided example.
4. If no alternative or error scenarios are explicitly specified in the provided use case, provide only the test case for the main flow.
5. Use the Italian language to describe the test case.
6. Do not include additional information or markdown formatting in your JSON response.

Here is an example of how to structure the JSON:

{{
  "TESTS": [
    {{
      "ID": "Acceptance Test ID, in the format TA-3 digit progressive",
      "DESCRIPTION": "brief but explanatory description of the test case, for example, Data Entry",
      "SC": "P if main flow, FA if Alternative Flow, FE if Exception Flow",
      "SS": "S if the flow simply includes another use case and does not add further specific steps, N otherwise",
      "ES": "S if the flow is explicitly present in the use case or if it is the main scenario, N otherwise",
      "UC": "use case ID"
    }}
  ]
}}

Respond only with the requested JSON without markdown and without adding other information. Always use the Italian language."""

SYSTEM_PRODUCE_UAT = """I will provide you with a use case and the identified acceptance test IDs. Act as a software engineer expert in test engineering to complete the acceptance test related to the use case. Respond with a well-formed JSON as in the following example.

EXAMPLE:
{{
  "PRECONDITION": "if SC='P' precondition of the use case, otherwise insert the steps of the main flow to be executed",
  "ACTORS": "list of actors of the use case",
  "TEST": [
    {{
      "STEP": "sequential numbering of the executed step",
      "INPUT": "input",
      "RESULT": "expected result of the step"
    }}
  ]
}}

Respond only with the JSON I requested, without adding any other information. Always use the Italian language."""

USER_PRODUCE_UAT = """#### START USE CASE
{UC}

#### END USE CASE
{output1}

Complete the acceptance test with ID = {ID_UAT}"""