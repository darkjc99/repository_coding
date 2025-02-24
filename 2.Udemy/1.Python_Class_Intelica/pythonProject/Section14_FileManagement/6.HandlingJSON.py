import json


# def get_json(file: str) -> dict:
#     with open(
#         file,
#         "r",
#     ) as file:
#         actual: dict = json.load(file)
#         return actual


# sample_date: dict = get_json(
#     "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/data.json"
# )
# print(sample_date)

sample: dict = {"name": "Elon", "age": 10, "has_mars": None}
# sample_json: str = json.dumps(sample)
# print(sample_json)

with open('E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/sample2.json', "w") as file:
    json.dump(sample, file)
