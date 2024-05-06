import os, json, pandas, tqdm

files = os.listdir("../제주도_데이터")[0:100]

fileLen = 0

for file in tqdm.tqdm(files):

    if fileLen <= 0:
        WordData = pandas.DataFrame(columns=['사투리','표준어']) # 전체 데이터
        Standard = pandas.DataFrame(columns=['사투리','표준어']) # 표준어
        Dialect = pandas.DataFrame(columns=['사투리','표준어']) # 사투리
    
    else:
        WordData = pandas.read_csv("../data/csv/전체_데이터.csv") # 전체 데이터
        Standard = pandas.read_csv("../data/csv/표준어.csv") # 표준어
        Dialect = pandas.read_csv("../data/csv/사투리.csv") # 사투리
    
    f = open(f"../제주도_데이터/{file}", "r", encoding="utf8")

    load = json.load(f)

    for utterance in load["utterance"]:
        for eojeolList in utterance["eojeolList"]:

            if eojeolList["isDialect"]:
                Dialect = Dialect._append({"사투리" : eojeolList["eojeol"], "표준어" : eojeolList["standard"]}, ignore_index=True)

            else:
                Standard = Standard._append({"사투리" : eojeolList["eojeol"], "표준어" : eojeolList["standard"]}, ignore_index=True)
        
        
        WordData = WordData._append({"사투리" : eojeolList["eojeol"], "표준어" : eojeolList["standard"]}, ignore_index=True)


        WordData.to_csv("../data/csv/전체_데이터.csv", index=False)
        Standard.to_csv("../data/csv/표준어.csv", index=False)
        Dialect.to_csv("../data/csv/사투리.csv", index=False)

    fileLen += 1