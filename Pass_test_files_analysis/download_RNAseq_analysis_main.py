# Главный модуль по анализу данных скачивания RNA-seq
""" Вывод в файл или командную строку списка папок и образцов имеющих
    нужный флаг статуса скачивания для выбранной директории. """

# Примеры команды запуска:
# python download_RNAseq_analysis_main.py ./project_data_folders/ ERR_downloads.txt ERR
# python download_RNAseq_analysis_main.py ./project_data_folders/ command_line OK

import os
import sys
# Импорт модуля по анализу содержимого папки.
import one_folder_analysis_functions

arguments = sys.argv
# Путь к главной директории с папками файлов логов.
main_dir_path = sys.argv[1]
# Путь к файлу выдачи или "command_line" для выдачи в командную строку.
output = sys.argv[2]
# Флаг, по которому искать файлы со статусом скачивания, например, "ERR" или "OK"
flag_sequence = sys.argv[3]

# Проверка формата выдачи.
if output == "command_line":
    screen_flag = 1
else:
    screen_flag = 0

# Проверка, что элемент главной директории является папкой и вызов ее анализа.
main_dir_content = os.listdir(main_dir_path)
main_dir_content.sort()
for dir_item in main_dir_content:
    if os.path.isdir(main_dir_path + dir_item):
        output_set_flag_samples_folder = one_folder_analysis_functions.check_folder(
            main_dir_path + dir_item + '/',
            flag_sequence)
        # Проверка наличия образцов с флагом ствтуса скачивания и их выдача.
        if len(output_set_flag_samples_folder):
            if (screen_flag):
                print('\n' + dir_item)
                for sample in sorted(output_set_flag_samples_folder):
                    print(sample)
            else:
                with open(output, "a") as output_file:
                    output_file.write('\n' + dir_item + '\n')
                    for sample in sorted(output_set_flag_samples_folder):
                        output_file.write(sample + '\n')
