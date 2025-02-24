import os

# if os.path.exists(
#     "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/hello.txt"
# ):
#     os.remove(
#         "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/hello.txt"
#     )

folder_name = "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/sample_folder/"
for file in os.listdir(folder_name):
    print(file)
    if os.path.exists(folder_name + file):
        print("Deleting ", file)
        os.remove(folder_name + file)

os.removedirs(folder_name)