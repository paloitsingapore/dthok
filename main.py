import csv
import json
import os
import platform
import time
import tkinter
from tkinter import font as tkFont
from functools import partial
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
#from ttkbootstrap import Style
from json2xml import json2xml
from json2xml.utils import readfromjson
from utility import jsonGenerator, datagenerator
import concurrent.futures
import multiprocessing
import threading


def open_file():
    global payload_file
    file_path = filedialog.askopenfilename(filetypes=[('JSON Files', '*json')])
    if file_path is not None:
        pass
    payload_file = file_path
    pl_text.insert(END, file_path)


def buildXML(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    buildJSON(noOfRecords, file_name, payload_file)
    jsondata = readfromjson(file_name + ".json")
    xmldata = json2xml.Json2xml(jsondata, wrapper="Data", pretty=True, attr_type=False).to_xml()
    myfile = open(file_name + ".xml", "w")
    myfile.write(str(xmldata))
    myfile.close
    if platform.system() != 'Linux':
        Label(main_window, text='XML Data Generated Successfully!', foreground='green').place(x=200, y=200)
        main_window.update()
        #time.sleep(3)
        #main_window.destroy()
    finish = time.perf_counter()
    print(f'XML Finished in {round(finish - start, 2)} second(s)')


def append_to_file(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    record = int(noOfRecords)
    header = False
    with open(file_name+".csv", 'w', newline='') as file:
        csv_file = csv.writer(file, delimiter=',')
        rows, columns = datagenerator(payload_file, record)
        for row in rows:
            if not header:
                csv_file.writerow([x.title() for x in columns])
                header = True
            csv_file.writerow(row)
    if platform.system() != 'Linux':
        Label(main_window, text='CSV Data Generated Successfully!', foreground='green').place(x=200, y=200)
        main_window.update()
        #time.sleep(3)
        #main_window.destroy()
    finish = time.perf_counter()
    print(f'CSV File Finished in {round(finish - start, 2)} second(s)')


def buildJSON(noOfRecords, file_name, payload_file):
    start = time.perf_counter()
    record = int(noOfRecords)
    with open(payload_file, 'rb') as j:
        json_data = json.load(j)
    arr = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(jsonGenerator, json_data, {'Id': i + 1}) for i in range(record)]
        for f in concurrent.futures.as_completed(results):
            arr.append(f.result())

    fh = open(file_name+".json", "w+")
    fh.write(json.dumps(arr))
    fh.close
    if platform.system() != 'Linux':
        Label(main_window, text='JSON Data Generated Successfully!', foreground='green').place(x=200, y=200)
        main_window.update()
        #time.sleep(3)
        #ws.destroy()
    finish = time.perf_counter()
    print(f'JSON File Finished in {round(finish - start, 2)} second(s)')

#if platform.system() != 'Linux':
if __name__ == '__main__':
    multiprocessing.freeze_support()
    #style = Style()
    #style = Style(theme='darkly')
    file_name = "BulkTestData"
    #main_window = style.master
    main_window = Tk()
    helv36 = tkFont.Font(family='Helvetica', size=10)

    main_window.title('Bulk_Data_Generator_PSTD_1.0')
    main_window.geometry('500x300')

    def_textbox = tkinter.StringVar()

    pl_label = tkinter.Label(main_window, text='JSON Payload :', font=helv36)
    pl_label.place(x=10, y=53)

    pl_text=Entry(main_window, width=35)
    pl_text.place(x=110, y=50)

    upldbtn = Button(main_window, text='Choose File', style='primary.TButton', command=lambda: open_file())
    upldbtn.place(x=370, y=50)

    record_label = Label(main_window, text='NO Of Records :', font=helv36)
    record_label.place(x=10, y=100)

    record_text=Entry(main_window, width=10)
    record_text.place(x=110, y=100)

    CSVGeneBtn = Button(main_window, text='Generate CSV', style='primary.TButton', command=lambda: append_to_file(noOfRecords=int(record_text.get()), file_name=file_name, payload_file=pl_text.get()))
    #CSVGeneBtn = Button(main_window, text='Generate CSV', style='primary.TButton',command=lambda: threading.Thread(target=append_to_file, args=[record_text.get(), file_name, pl_text.get()]).start())
    CSVGeneBtn.place(x=80, y=150)

    jsonGeneBtn = Button(main_window, text='Generate JSON', style='primary.TButton', command=lambda: buildJSON(noOfRecords=int(record_text.get()), file_name=file_name, payload_file=pl_text.get()))
    #jsonGeneBtn = Button(main_window, text='Generate JSON', style='primary.TButton',command=lambda: threading.Thread(target=buildJSON,args=[record_text.get(), file_name, pl_text.get()]).start())
    jsonGeneBtn.place(x=200, y=150)

    xmlGeneBtn = Button(main_window, text='Generate XML', style='primary.TButton', command=lambda: buildXML(noOfRecords=int(record_text.get()), file_name=file_name, payload_file=pl_text.get()))
    #xmlGeneBtn = Button(main_window, text='Generate XML', style='primary.TButton',command=lambda: threading.Thread(target=buildXML,args=[record_text.get(), file_name, pl_text.get()]).start())
    xmlGeneBtn.place(x=330, y=150)

    exit_button = Button(main_window, text="Close", style='primary.TButton', command=main_window.destroy)
    exit_button.place(x=400, y=250)

    main_window.mainloop()