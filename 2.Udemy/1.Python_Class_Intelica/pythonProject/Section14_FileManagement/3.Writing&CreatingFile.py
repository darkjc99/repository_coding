# with open(
#     "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/sample.txt",
#     "a+",
# ) as text:
#     # text.write("\nNew Text")

#     text.write("12345")
#     text.seek(0)
#     print(text.read())


# with open(
#     "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/name.txt",
#     "w+",
# ) as text:
#     text.write("REPLACING")
#     text.seek(0)
#     print(text.read())

with open(
    "E:/Codeando/repository_coding/2.Udemy/1.Python_Class_Intelica/pythonProject/Section14_FileManagement/hello.txt",
    "x+",
) as text:
    text.write("Hello World")
    text.seek(0)
    print(text.read())
