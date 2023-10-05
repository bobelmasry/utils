import json

# num of years Default is 12 when starts from 2011 and ends in 2022
url = 'https://papers.gceguide.com'
db = open('data.json', 'w')
subjects = [{"subjectname" : "physics", "subject" : 'Physics%20(9702)', "hasMarch" : True, "PCode" : 9702, "Papers" : [1,2,3,4,5], "numofyears" : 12, "solvePapers" : ['11','12','13'], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "biology", "subject" : 'Biology%20(9700)', "hasMarch" : True, "PCode" : 9700, "Papers" : [1,2,3,4,5], "numofyears" : 12, "solvePapers" : ['11','12','13'], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "chemistry", "subject" : 'Chemistry%20(9701)', "hasMarch" : True, "PCode" : 9701, "Papers" : [1,2,3,4,5], "numofyears" : 12, "solvePapers" : ['11','12','13'], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "economics", "subject" : 'Economics%20(9708)', "hasMarch" : True, "PCode" : 9708, "Papers" : [1,2,3,4], "numofyears" : 12, "solvePapers" : ['11','12','13','31','32','33'], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "business", "subject" : 'Business%20(9609)', "hasMarch" : True, "PCode" : 9609, "Papers" : [1,2,3], "numofyears" : 7, "solvePapers" : [''], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "computer-science", "subject" : 'Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)', "hasMarch" : False, "PCode" : 9618, "Papers" : [1,2,3,4], "numofyears" : 2, "solvePapers" : [''], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "english-language", "subject" : 'English%20Language%20(9093)', "hasMarch" : True, "PCode" : 9093, "Papers" : [1,2,3,4], "numofyears" : 9, "solvePapers" : [''], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "history", "subject" : 'History%20(9489)', "hasMarch" : True, "PCode" : 9489, "Papers" : [1,2,3,4], "numofyears" : 3, "solvePapers" : [''], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "math", 'subject' : 'Mathematics%20(9709)', "hasMarch" : True, "PCode" : 9709, "Papers" : [1,2,3,4,5,6], "numofyears" : 12, 'solvePapers' : [''], "Level" : "A-level", "url2" : "A%20Levels"},
            {"subjectname" : "physics", 'subject' : 'Physics%20(0625)', "hasMarch" : True, "PCode" : '0625', "Papers" : [1,2,3,4,5,6], "numofyears" : 12,"solvePapers" : ['11','12','13','21','22','23'], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "biology", "subject" : "Biology%20(0610)", "hasMarch" : True, "PCode" : '0610', "Papers" : [1,2,3,4,5,6], "numofyears" : 12,"solvePapers" : ['11','12','13','21','22','23'], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "chemsitry", "subject" : 'Chemistry%20(0620)', "hasMarch" : True, "PCode" : '0620', "Papers" : [1,2,3,4,5,6], "numofyears" : 12,"solvePapers" : ['11','12','13','21','22','23'], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "economics", "subject" : 'Economics%20(0455)', "hasMarch" : True, "PCode" : '0455', "Papers" : [1,2], "numofyears" : 12, "solvePapers" : ['11','12','13'], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "business", "subject" : "Business%20Studies%20(0450)", "hasMarch" : True, "PCode" : '0450', "Papers" : [1,2], "numofyears" : 12, "solvePapers" : [''], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "computer-science", "subject" : "Computer%20Science%20(0478)", "hasMarch" : True, "PCode" : '0478', "Papers" : [1,2], "numofyears" : 8, "solvePapers" : [''], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "english-language", "subject" : "English%20-%20First%20Language%20(0500)", "hasMarch" : True, "PCode" : '0500', "Papers" : [1,2], "numofyears" : 9, "solvePapers" : [''], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "history", "subject" : "History%20(0470)", "hasMarch" : True, "PCode" : '0470', "Papers" : [1,2,4], "numofyears" : 12, "solvePapers" : [''], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"},
            {"subjectname" : "math", "subject" : "Mathematics%20(0580)", "hasMarch" : True, "PCode" : '0580', "Papers" : [1,2,3,4], "numofyears" : 12, "solvePapers" : [''], "Level" : "IGCSE", "url2" : "Cambridge%20IGCSE"}]

for subjectCounter in range(len(subjects)):
    currentSubject = subjects[subjectCounter]
    print(currentSubject['PCode'])
    for i in range(currentSubject['numofyears']):
        if (((22-i) > 15) and currentSubject['hasMarch'] == True ):
            for mcounter in range(len(currentSubject['Papers'])):
                paperObject = {
                                "slug" : f"{str(currentSubject['PCode'])}_m{str(22-i)}_ms_{str(currentSubject['Papers'][mcounter])}2",
                                "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_ms_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                "name":f"Paper {str(mcounter+1)} Variant 2",
                                "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_qp_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                "isMs":"True",
                                "year":f"20{str(22-i)}",
                                "subjectName":currentSubject['subjectname'],
                                "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][mcounter])}2/F/M/{str(22-i)} ms",
                                "hasSolve" : "False",
                                "Level" : currentSubject['Level']
                            }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    
                if (f"{str(currentSubject['Papers'][mcounter])}2" in currentSubject['solvePapers']) and (22-i >= 17):
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_m{str(22-i)}_qp_{str(currentSubject['Papers'][mcounter])}2",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_qp_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                    "name":f"Paper {str(mcounter+1)} Variant 2",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_ms_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][mcounter])}2/F/M/{str(22-i)} qp",
                                    "hasSolve" : "True",
                                    "Level" : currentSubject['Level']
                                }
                else: 
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_m{str(22-i)}_qp_{str(currentSubject['Papers'][mcounter])}2",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_qp_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                    "name":f"Paper {str(mcounter+1)} Variant 2",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_m{str(22-i)}_ms_{str(currentSubject['Papers'][mcounter])}2.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][mcounter])}2/F/M/{str(22-i)} qp",
                                    "hasSolve" : "False",
                                    "Level" : currentSubject['Level']
                                }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    




        for scounter in range(len(currentSubject['Papers'])):
            for variant in range(3):
                paperObject = {
                                "slug" : f"{str(currentSubject['PCode'])}_s{str(22-i)}_ms_{str(currentSubject['Papers'][scounter])}{str(variant+1)}",
                                "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_ms_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(scounter +1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_qp_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                "isMs":"True",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{currentSubject['subjectname']}",
                                "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][scounter])}{str(variant+1)}/M/J/{str(22-i)} ms",
                                "hasSolve" : "False",
                                "Level" : currentSubject['Level']
                            }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    

                if (f"{str(currentSubject['Papers'][scounter])}{str(variant+1)}" in currentSubject['solvePapers']) and (22-i >= 17):
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_s{str(22-i)}_qp_{str(currentSubject['Papers'][scounter])}{str(variant+1)}",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_qp_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                    "name":f"Paper {str(scounter+1)} Variant {str(variant+1)}",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_ms_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][scounter])}{str(variant+1)}/M/J/{str(22-i)} qp",
                                    "hasSolve" : "True",
                                    "Level" : currentSubject['Level']
                                }
                else:
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_s{str(22-i)}_qp_{str(currentSubject['Papers'][scounter])}{str(variant+1)}",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_qp_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                    "name":f"Paper {str(scounter+1)} Variant {str(variant+1)}",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_s{str(22-i)}_ms_{str(currentSubject['Papers'][scounter])}{str(variant+1)}.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][scounter])}{str(variant+1)}/M/J/{str(22-i)} qp",
                                    "hasSolve" : "False",
                                    "Level" : currentSubject['Level']
                                }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    



        for wcounter in range(len(currentSubject['Papers'])):
            for variant in range(3):
                paperObject = {
                                "slug" : f"{str(currentSubject['PCode'])}_w{str(22-i)}_ms_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}",
                                "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_ms_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_qp_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                "isMs":"True",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{currentSubject['subjectname']}",
                                "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][wcounter])}{str(variant+1)}/O/N/{str(22-i)} ms",
                                "hasSolve" : "False",
                                "Level" : currentSubject['Level']
                            }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    

                if (f"{str(currentSubject['Papers'][wcounter])}{str(variant+1)}" in currentSubject['solvePapers']) and (22-i >= 17):
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_w{str(22-i)}_qp_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_qp_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                    "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_ms_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][wcounter])}{str(variant+1)}/O/N/{str(22-i)} qp",
                                    "hasSolve" : "True",
                                    "Level" : currentSubject['Level']
                                }
                else:
                    paperObject = {
                                    "slug" : f"{str(currentSubject['PCode'])}_w{str(22-i)}_qp_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}",
                                    "src": f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_qp_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                    "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                                    "msSrc":f"{url}/{currentSubject['url2']}/{currentSubject['subject']}/20{str(22-i)}/{str(currentSubject['PCode'])}_w{str(22-i)}_ms_{str(currentSubject['Papers'][wcounter])}{str(variant+1)}.pdf",
                                    "isMs":"False",
                                    "year":f"20{str(22-i)}",
                                    "subjectName":f"{currentSubject['subjectname']}",
                                    "synonym" : f"{str(currentSubject['PCode'])}/{str(currentSubject['Papers'][wcounter])}{str(variant+1)}/O/N/{str(22-i)} qp",
                                    "hasSolve" : "False",
                                    "Level" : currentSubject['Level']
                                }
                paperObjectFormatted = json.dumps(paperObject)
                db.write(paperObjectFormatted)
                db.write(",\n")    


db.close()