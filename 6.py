import json

PCode=9702
Papers= [1,2,3,4,5]
numofyears = 12 # Default is 12 when starts from 2011 and ends in 2022
url = 'https://papers.gceguide.com'
type = 'A%20Levels'
subject = 'Physics%20(9702)'
subjectname = 'physics'
db = open('data2.json', 'w')
hasMarch = True
solvePapers = ['11','12','13']


for i in range(numofyears):
    if (((22-i) > 15) and hasMarch == True ):
        for mcounter in range(len(Papers)):
            paperObject = {
                            "slug" : f"{str(PCode)}_m{str(22-i)}_ms_{str(Papers[mcounter])}2",
                            "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_ms_{str(Papers[mcounter])}2.pdf",
                            "name":f"Paper {str(mcounter+1)} Variant 2",
                            "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_qp_{str(Papers[mcounter])}2.pdf",
                            "isMs":"True",
                            "year":f"20{str(22-i)}",
                            "subjectName":f"{subjectname}",
                            "synonym" : f"{str(PCode)}/{str(Papers[mcounter])}2/F/M/{str(22-i)} ms",
                            "hasSolve" : "False"
                        }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")    
            if (f"{str(Papers[mcounter])}2" in solvePapers) and (22-i >= 17):
                paperObject = {
                                "slug" : f"{str(PCode)}_m{str(22-i)}_qp_{str(Papers[mcounter])}2",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_qp_{str(Papers[mcounter])}2.pdf",
                                "name":f"Paper {str(mcounter+1)} Variant 2",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_ms_{str(Papers[mcounter])}2.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[mcounter])}2/F/M/{str(22-i)} qp",
                                "hasSolve" : "True"
                            }
            else: 
                paperObject = {
                                "slug" : f"{str(PCode)}_m{str(22-i)}_qp_{str(Papers[mcounter])}2",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_qp_{str(Papers[mcounter])}2.pdf",
                                "name":f"Paper {str(mcounter+1)} Variant 2",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_m{str(22-i)}_ms_{str(Papers[mcounter])}2.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[mcounter])}2/F/M/{str(22-i)} qp",
                                "hasSolve" : "False"
                            }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")



    for scounter in range(len(Papers)):
        for variant in range(3):
            paperObject = {
                            "slug" : f"{str(PCode)}_s{str(22-i)}_ms_{str(Papers[scounter])}{str(variant+1)}",
                            "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_ms_{str(Papers[scounter])}{str(variant+1)}.pdf",
                            "name":f"Paper {str(scounter+1)} Variant {str(variant+1)}",
                            "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_qp_{str(Papers[scounter])}{str(variant+1)}.pdf",
                            "isMs":"True",
                            "year":f"20{str(22-i)}",
                            "subjectName":f"{subjectname}",
                            "synonym" : f"{str(PCode)}/{str(Papers[scounter])}{str(variant+1)}/M/J/{str(22-i)} ms",
                            "hasSolve" : "False"
                        }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")
            if (f"{str(Papers[scounter])}{str(variant+1)}" in solvePapers) and (22-i >= 17):
                paperObject = {
                                "slug" : f"{str(PCode)}_s{str(22-i)}_qp_{str(Papers[scounter])}{str(variant+1)}",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_qp_{str(Papers[scounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(scounter+1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_ms_{str(Papers[scounter])}{str(variant+1)}.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[scounter])}{str(variant+1)}/M/J/{str(22-i)} qp",
                                "hasSolve" : "True"
                            }
            else:
                paperObject = {
                                "slug" : f"{str(PCode)}_s{str(22-i)}_qp_{str(Papers[scounter])}{str(variant+1)}",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_qp_{str(Papers[scounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(scounter+1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_s{str(22-i)}_ms_{str(Papers[scounter])}{str(variant+1)}.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[scounter])}{str(variant+1)}/M/J/{str(22-i)} qp",
                                "hasSolve" : "False"
                            }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")


    for wcounter in range(len(Papers)):
        for variant in range(3):
            paperObject = {
                            "slug" : f"{str(PCode)}_w{str(22-i)}_ms_{str(Papers[wcounter])}{str(variant+1)}",
                            "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_ms_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                            "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                            "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_qp_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                            "isMs":"True",
                            "year":f"20{str(22-i)}",
                            "subjectName":f"{subjectname}",
                            "synonym" : f"{str(PCode)}/{str(Papers[wcounter])}{str(variant+1)}/O/N/{str(22-i)} ms",
                            "hasSolve" : "False"
                        }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")
            if (f"{str(Papers[wcounter])}{str(variant+1)}" in solvePapers) and (22-i >= 17):
                paperObject = {
                                "slug" : f"{str(PCode)}_w{str(22-i)}_qp_{str(Papers[wcounter])}{str(variant+1)}",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_qp_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_ms_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[wcounter])}{str(variant+1)}/O/N/{str(22-i)} qp",
                                "hasSolve" : "True"
                            }
            else:
                paperObject = {
                                "slug" : f"{str(PCode)}_w{str(22-i)}_qp_{str(Papers[wcounter])}{str(variant+1)}",
                                "src": f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_qp_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                                "name":f"Paper {str(wcounter+1)} Variant {str(variant+1)}",
                                "msSrc":f"{url}/{type}/{subject}/20{str(22-i)}/{str(PCode)}_w{str(22-i)}_ms_{str(Papers[wcounter])}{str(variant+1)}.pdf",
                                "isMs":"False",
                                "year":f"20{str(22-i)}",
                                "subjectName":f"{subjectname}",
                                "synonym" : f"{str(PCode)}/{str(Papers[wcounter])}{str(variant+1)}/O/N/{str(22-i)} qp",
                                "hasSolve" : "False"
                            }
            paperObjectFormatted = json.dumps(paperObject)
            db.write(paperObjectFormatted)
            db.write(""",
""")



db.close()