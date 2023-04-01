import csv
import os


def extract_taxon(taxon_path):
    All_taxon = list()
    with open(taxon_path) as f:
        while True:
            my_line = f.readline()
            if my_line:
                All_taxon.append(my_line.strip("\n"))
            else:
                return All_taxon
                break


def count_taxon(tabular_file, taxon_members):
    elements = list(len(taxon_members))
    for i in len(taxon_members):
        # elements[i] =
        pass


if __name__ == '__main__':
    All_classes = extract_taxon("/media/davidfdr99/WD_NiGo/D4GEN-2023/data/Counting/Colclass.list")
    All_orders = extract_taxon("/media/davidfdr99/WD_NiGo/D4GEN-2023/data/Counting/Colorder.list")
    All_families = extract_taxon("/media/davidfdr99/WD_NiGo/D4GEN-2023/data/Counting/Colfamily.list")
    All_genera = extract_taxon("/media/davidfdr99/WD_NiGo/D4GEN-2023/data/Counting/Colgenus.list")
    with open("/media/davidfdr99/WD_NiGo/D4GEN-2023/data/Unique_taxonKey.tsv", 'r') as file:
        Unique_Mollusca = file.readlines()
    all_classes = []
    for line in Unique_Mollusca:
        cols = line.strip('\n').split('\t')
        all_classes.append(cols[3])
    final_list = []
    only_one_class = list(set(all_classes))
    for elm in only_one_class:
        nb_iteration = all_classes.count(elm)
        final_list.append([elm, nb_iteration])
    with open('phylo_data/gene.tsv', 'w', newline='') as file:
        content = csv.writer(file, delimiter='\t')
        content.writerows(final_list)



