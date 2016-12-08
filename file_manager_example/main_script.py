# coding: utf-8
"""Main module of course project.
 Summary - intended to move media files from source to destination.
 Various arguments are applied:
 1) Type of media to move: 'audio', 'image', 'video'
 2) 'source_path' and 'destination'
 3) Recursion limit: 'count'
 4) sorting in destination path: 'formatting'
 5) Safe or usual delete method: 'safe_delete'

 Logging is always True

 Accepts Namespace from args_module.py
"""

import args_module
import media_extensions
import os
import logging
import shutil
import sys
import time


def media_selection(video, audio, image):
    """Takes one True argument.
    Returns one of three media types for search_and_copy function"""

    media_type = None

    if video:
        media_type = media_extensions.video_extensions_example()
    if audio:
        media_type = media_extensions.audio_extensions_example()
    if image:
        media_type = media_extensions.image_extensions_example()

    return media_type


def search_and_copy(source, destination, media, recursion):
    """Function for parsing media content in source folder and copying
    unique files to destination folder. Finding duplicates of files."""

    sys.setrecursionlimit(recursion)
    file_list = []  # file list of all files of selected media used for further delete in save_and_delete func
    new_file_list = []  # temporary file list of unique files

    for path, folders, files in os.walk(source):
        for file in files:
            file_path = str(os.path.join(path, file))
            if (os.path.basename(file_path).split(".", -1)[1]) in media:
                file_list.append(file_path)

    for source_files in file_list:
        b = os.path.basename(source_files)
        if b not in new_file_list:
            new_file_list.append(b)
            new_file_list.append(source_files)
        else:
            logging.debug("Duplicate found: {}".format(source_files))

    file_list_to_copy = [file for file in new_file_list if os.path.isfile(file)]

    for file in file_list_to_copy:
        logging.info("Copy: '{}' to {}".format(os.path.basename(file), destination_path))
        if os.path.isfile(file):
            try:
                shutil.copy2(file, destination)
            except OSError as why:
                logging.debug(why)
                if not os.path.isdir(destination):
                    os.makedirs(destination)
                    shutil.copy2(file, destination)

    return file_list


def safe_delete(files, key):
    """Function for safe delete, if key=True safe delete, otherwise usual delete"""

    from send2trash import send2trash
    for file in files:
        logging.info('File deleted: {}'.format(file))
        if key:
            try:
                send2trash(file)
            except OSError as why:
                logging.debug(why)
        else:
            os.remove(file)


def sorting(destination, key):
    """Function for hardcoded sorting of files by folders in destination path"""

    from string import digits

    if key:
        for path, folders, files in os.walk(destination):
            for file in files:
                if file.startswith(("a", "b", "c", "d", "e", "f", "g", "h")):
                    os.makedirs(destination + os.sep + "a-h", exist_ok=True)
                    shutil.move(os.path.join(destination, file), os.path.join((destination + "a-h"), file.lower()))
                    logging.info("File {} moved to {}".format(file, os.path.abspath(destination + os.sep + "a-h")))
                elif file.startswith(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")):
                    os.makedirs(destination + os.sep + "i-r", exist_ok=True)
                    shutil.move(os.path.join(destination, file), os.path.join((destination + "i-r"), file.lower()))
                    logging.info("File {} moved to {}".format(file, os.path.abspath(destination + os.sep + "i-r")))
                elif file.startswith(("s", "t", "u", "v", "w", "x", "y", "z")):
                    os.makedirs(destination + os.sep + "s-z", exist_ok=True)
                    shutil.move(os.path.join(destination, file), os.path.join((destination + "s-z"), file.lower()))
                    logging.info("File {} moved to {}".format(file, os.path.abspath(destination + os.sep + "s-z")))
                elif file.startswith(tuple(digits)):
                    os.makedirs(destination + os.sep + "0-9", exist_ok=True)
                    shutil.move(os.path.join(destination, file), os.path.join((destination + "0-9"), file.lower()))
                    logging.info("File {} moved to {}".format(file, os.path.abspath(destination + os.sep + "0-9")))
                else:
                    os.makedirs(destination + os.sep + "unsorted", exist_ok=True)
                    shutil.move(os.path.join(destination, file), os.path.join((destination + "unsorted"), file.lower()))
                    logging.info("File {} moved to {}".format(file, os.path.abspath(destination + os.sep + "unsorted")))


def smart_sorting(destination, key):
    """Second type of sorting function. It has to sort in maximum
    of 8 folders for latin, 8 folders for cyrillic, one for digits and one
    for unsorted. Sorting and folder names are named by first letters
    of file name.
    NOT YET IMPLEMENTED!!!
    """

    if key:
        first_letters_list = []
        for path, folders, files in os.walk(destination):
            for file in files:
                if file[0] in first_letters_list:
                    pass
                else:
                    first_letters_list.append(file[0])

        if len(first_letters_list) <= 8:
            for future_folders in first_letters_list:
                os.makedirs(os.path.abspath(destination) + os.sep + future_folders + os.sep)


if __name__ == "__main__":

    parser = args_module.get_arguments()
    source_path = os.path.abspath(parser['source_path']) + os.sep
    destination_path = os.path.abspath(parser['destination']) + os.sep
    # parser['image'] = True  # hardcoded option, for simplicity of debugging of main_script (will be deleted afterwards)

    os.makedirs(os.path.abspath(os.curdir) + os.sep + "logs" + os.sep, exist_ok=True)

    logging.basicConfig(level=logging.DEBUG, format=u"%(filename)s[LINE:%(lineno)d]# %(levelname)-8s"
                                                    u" [%(asctime)s]  %(message)s",
                        filename=os.path.abspath(os.curdir) + os.sep + "logs" + os.sep + "{}.txt"
                        .format(time.strftime('%Y_%b_%d_%H_%M_%S')))

    logging.info('Start of program')

    returned_media_type = media_selection(parser['video'], parser['audio'], parser['image'])
    returned_file_list = search_and_copy(source_path, destination_path, returned_media_type, int(parser['count']))

    safe_delete(returned_file_list, parser['safe_delete'])
    sorting(destination_path, parser['formatting'])
    # smart_sorting(destination_path, parser['formatting']) # not yet implemented

    logging.info('End of program')
