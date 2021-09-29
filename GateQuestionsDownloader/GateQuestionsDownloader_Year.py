import requests

URL = "https://gate.iitkgp.ac.in/documents/gatepapers/%s/%s_%s.pdf"
SubjectCode = "cs"
yearsList = [2017, 2021]

for year in yearsList :
    fileURL = URL % (year, SubjectCode, year)
    try :
        response = requests.get(fileURL)
        fileName = SubjectCode + str(year) + ".pdf"
        if response.status_code == 200 :
            with open(fileName, "wb") as file :
                file.write(response.content)
            print("[+]", fileName, "Downloaded")
        else :
            raise Exception(response.text)
    except Exception as Err :
        print("[x]", fileName, "Error")

