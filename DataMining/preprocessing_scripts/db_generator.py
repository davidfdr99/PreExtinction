import os
import csv
from tqdm import tqdm


def generate_database():
    # CLASS
    a_class = []
    with open("data/phylo_data/classes.tsv", 'r') as file:
        content = file.readlines()
    for line in content[1:]:
        cols = line.strip('\n').split('\t')
        a_class.append(cols)
    # ORDER
    a_order = []
    with open("data/phylo_data/orders.tsv", 'r') as file:
        content = file.readlines()
    for line in content[1:]:
        cols = line.strip('\n').split('\t')
        a_order.append(cols)
    # FAMILY
    a_family = []
    with open("data/phylo_data/families.tsv", 'r') as file:
        content = file.readlines()
    for line in content[1:]:
        cols = line.strip('\n').split('\t')
        a_family.append(cols)
    # GENUS
    a_genus = []
    with open("data/phylo_data/gene.tsv", 'r') as file:
        content = file.readlines()
    for line in content[1:]:
        cols = line.strip('\n').split('\t')
        a_genus.append(cols)
    #
    format_content = []
    # class, order, family, genus, species, decimalLatitude, decimalLongitude, elevation, depth, year, taxonKey
    with open("data/Subset_Columns_Mollusca.tsv", 'r') as file:
        content = file.readlines()
    for line in content[1:]:
        cols = line.strip('\n').split('\t')
        format_content.append(cols)
    for species in tqdm(iterable=os.listdir('data/all_no_process'), desc='process'):  # change subset_all to all
        all_year = []
        all_year_only_species = []
        all_status = []
        final_list = []
        with open(f'data/all_no_process/{species}', 'r') as file:
            content_species = []
            content = file.readlines()
            for line in content[1:]:
                cols = line.strip('\n').split('\t')
                s_scientific_name = cols[0]
                all_status.append([cols[1], cols[2]])
                all_year_only_species.append(int(cols[1]))
                nb_native = cols[3]
                nb_present = cols[4]
                nb_vagrant = cols[5]
                content_species.append(cols)
        for line in format_content:
            if line[4] == s_scientific_name:
                if line[9] != '':
                    if line[9] not in all_year:
                        final_list.append(line)
                        all_year.append(line[9])
                elif line[5] != '' and line[6] != '':
                    for tp in final_list:
                        if tp[5] == '' and tp[6] == '':
                            tp[5] = line[5]
                            tp[6] = line[6]
                        break
        for tp in final_list:
            s_class = tp[0]
            for c in a_class:
                if s_class == c[0]:
                    nb_class = c[1]
            s_order = tp[1]
            for o in a_order:
                if s_order == o[0]:
                    nb_order = o[1]
            s_family = tp[2]
            for f in a_family:
                if s_family == f[0]:
                    nb_family = f[1]
            s_genus = tp[3]
            for g in a_genus:
                if s_genus == g[0]:
                    nb_genus = g[1]
            tp.append(nb_native)
            tp.append(nb_present)
            tp.append(nb_vagrant)
            tp.append(nb_class)
            tp.append(nb_order)
            tp.append(nb_family)
            tp.append(nb_genus)
        all_year_only_species = sorted(all_year_only_species)
        for line in final_list:
            if len(all_year_only_species) == 1:
                line.append(all_status[0][1])
            else:
                for year in all_year_only_species:
                    index_year = 0
                    if int(line[9]) >= year:
                        index_year += 1
                    else:
                        break
                line.append(all_status[index_year][1])
        if final_list != [[]]:
            with open(f'data/process_data/{species.replace(" ", "_")}', 'w', newline='') as file:
                content = csv.writer(file, delimiter='\t')
                content.writerows(final_list)


if __name__ == '__main__':
    print('start')
    generate_database()
    print('end')
