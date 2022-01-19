
#!/usr/bin/python3

import http.client as http
import json
import argparse




api_key = 'YOUR API KEY'


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def save(result,file_name):
    with open(file_name,'w') as f: 
    
        result = result.replace('"','')
        result = result.replace('[','')
        result = result.replace(' ','')
        result = result.replace(']','')
        result = result.replace(',','')
        f.write(result)
    

def get_arg ():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-i','--input', help='Enter domain or E-mail or etc for reverse whois', required=True)
    parser.add_argument('-f','--file', help='File name for saving domains', required=True)
    args=vars(parser.parse_args())

    return  args


def generate_payload(input):

    payload_basic = {
        'basicSearchTerms': {
            'include': [
                input  
            ]
         
        },
        'searchType': 'current',
        
        'mode': 'purchase',
        'apiKey': api_key,
        'responseFormat': 'json'
    }

    return payload_basic

def json_parse(response):

    response_json = json.loads(response)["domainsList"]
    
    result = json.dumps(response_json, indent=4, sort_keys=True)
    return result


def end_request(arg):
    # print(payload_basic)
    conn = http.HTTPSConnection('reverse-whois.whoisxmlapi.com')

    # Basic search
    payload = generate_payload(arg)
    conn.request('POST', '/api/v2', json.dumps(payload), headers)

    response = conn.getresponse()
    text = response.read().decode('utf8')

    return text

    # print_response(text)

if __name__ == '__main__':

    input = get_arg()['input']
    file  = get_arg()['file']
    request_result = end_request(input)
    json_result = json_parse(request_result)
    save(json_result, file)



   
