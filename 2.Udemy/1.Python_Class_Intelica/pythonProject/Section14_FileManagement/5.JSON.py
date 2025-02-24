import json

with open(
    "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/sample.json"
) as file:
    content: dict = json.load(file)
    print(content)