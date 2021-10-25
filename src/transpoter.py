import csv
import json
import time
import concurrent.futures
from json2xml import json2xml
from json2xml.utils import readfromjson
from src.utility import jsonGenerator, datagenerator

def buildXML(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    buildJSON(noOfRecords, file_name, payload_file)
    jsondata = readfromjson(file_name + ".json")
    xmldata = json2xml.Json2xml(jsondata, wrapper="Data", pretty=True, attr_type=False).to_xml()
    myfile = open(file_name + ".xml", "w")
    myfile.write(str(xmldata))
    myfile.close
    finish = time.perf_counter()
    print(f'XML Finished in {round(finish - start, 2)} second(s)')


def append_to_file(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    record = int(noOfRecords)
    header = False
    with open(file_name+".csv", 'w') as file:
        csv_file = csv.writer(file, delimiter=',')
        rows, columns = datagenerator(payload_file, record)
        for row in rows:
            if not header:
                csv_file.writerow([x.title() for x in columns])
                header = True
            csv_file.writerow(row)
    finish = time.perf_counter()
    print(f'CSV File Finished in {round(finish - start, 2)} second(s)')


def buildJSON(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    record = int(noOfRecords)
    with open(payload_file, 'rb') as j:
        json_data = json.load(j)
    arr = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(jsonGenerator, json_data, {'id': i + 1}) for i in range(record)]
        for f in concurrent.futures.as_completed(results):
            arr.append(f.result())

    fh = open(file_name+".json", "w+")
    fh.write(json.dumps(arr))
    fh.close
    finish = time.perf_counter()
    print(f'JSON File Finished in {round(finish - start, 2)} second(s)')