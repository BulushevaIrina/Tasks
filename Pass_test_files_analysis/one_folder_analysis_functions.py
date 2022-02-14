# Модуль функций по анализу содержимого папки.

import os

def check_folder(path_to_folder, flag_downloaded):
    """ Анализ папки на наличие файлов report...txt и вызов их анализа.
        Возвращение общего списка образцов папки имеющих флаг"""
    folder_content = os.listdir(path_to_folder)
    folder_content.sort()
    set_of_flag_samples_folder = set()
    for item in folder_content:
        if item.startswith('report') and item.endswith('.txt'):
            set_of_flag_samples_folder = set.union(
                set_of_flag_samples_folder,
                report_file_analysis(path_to_folder + item, flag_downloaded)
            )
    return (set_of_flag_samples_folder)

def take_sample_name_from_file_name (file_path):
    """ Возвращение названия образца по его пути. """
    if "/" in file_path:
        file_name = file_path.split('/')[-1]
    else:
        file_name = file_path
    if "_" in file_name:
        sample_name = file_name.split('_')[0]
    else:
        sample_name = file_name.split('.')[0]
    return(sample_name)

def report_file_analysis(report_file_path, flag_downloaded):
    """ Возвращение списка образцов имеющих флаг из файла report. """
    set_of_flag_samples_file = set()
    report_file = open(report_file_path, "r")
    report_file_lines = report_file.readlines()
    for line_index in range (len(report_file_lines)):
        if "Download Results:" in report_file_lines[line_index]:
            list_download_info = report_file_lines[line_index + 3].split('|')
            # Проверка флага статуса скачивания образца.
            if list_download_info[1].strip() == flag_downloaded:
                set_of_flag_samples_file.add(take_sample_name_from_file_name(\
                                            list_download_info[3].rstrip("\n")))
    return(set_of_flag_samples_file)
