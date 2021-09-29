import requests

URL = "https://gate.iitkgp.ac.in/documents/gatepapers/%s/%s_%s.pdf"
SubjectCode = "cs"
yearStarting = 2007
yearEnding = 2021

for year in range(yearStarting, yearEnding + 1) :
    fileURL = URL % (year, SubjectCode, year)
    try :
        response = requests.get(fileURL, stream=True)
        if response.status_code == 200 :
            fileName = SubjectCode + str(year) + ".pdf"
            with open(fileName, "wb") as file :
                file.write(response.content)
            print("[+]", fileName, "Downloaded")
        else :
            raise Exception("Error")
    except :
        print("[x]", fileName, "Error")
