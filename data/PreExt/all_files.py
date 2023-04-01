import os


def final_format():
    format_content = []
    with open("Subset_Columns_Mollusca.tsv", 'r') as file:
        content = file.readlines()
    for line in content:
        print(content)
    for species in os.listdir('path'):
        pass


final_format()