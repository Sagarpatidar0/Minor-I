def translate(df=None):
    import requests, uuid, json

    # Add your key and endpoint
    key = "002c43301bf74ccfa3539904e13f8904"
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    location = "eastus2"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'hi',
        'to': 'en'
     }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = []
    for i in range(len(df)):
        body.append({'text': df['comment'][i]})

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    data = (json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    comment_translated = []
    for i in range(len(response)):
        comment_translated.append(response[i]['translations'][0]['text'])

    return comment_translated
