import requests, json, time

def run(year, month):
    has_next = True
    #url = "https://jarbas.serenatadeamor.org/api/chamber_of_deputies/reimbursement/?year=%s&month=%s" % (year, month)
    url = "https://jarbas.serenatadeamor.org/api/chamber_of_deputies/reimbursement/?limit=7&month=10&offset=945&year=2017"

    while(has_next):
        response = requests.get(url)

        if response.status_code != 200:
            print(url)
            raise Exception(response.content)

        response_obj = json.loads(response.content)
        
        if response_obj['next']:
            url = response_obj['next']
        else:
            has_next = False

        for result in response_obj['results']:
            line = "%s,%s,%s,%s,%s\n" % (result['congressperson_name'], result['subquota_description'].replace(',', ''), result['party'], result['state'], result['document_value'])

            with open('csvfile.csv','a') as file:
                file.write(line)

run(2017, 10)
