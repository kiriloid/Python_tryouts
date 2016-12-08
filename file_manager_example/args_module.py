# -*- coding: utf-8 -*-
""" Module for parsing arguments for main_script.py
Returns Namespace of args:
{'audio': False,
 'count': 50,
 'destination': 'D:\\untitled\\course_project\\destination\\',
 'formatting': True,
 'image': False,
 'safe_delete': False,
 'source_path': 'D:\\untitled\\course_project\\content\\',
 'video': False}
"""


import argparse
import os


if __name__ != "__main__":
    parser = argparse.ArgumentParser()

    """
    In this block user have to choose one of media type for future copying
    """

    choice_options = parser.add_mutually_exclusive_group(required=False)

    choice_options.add_argument("-v", "--video", action="store_true", default=False,
                                help="Argument to select video files")
    choice_options.add_argument("-a", "--audio", action="store_true", default=False,
                                help="Argument to select audio files")
    choice_options.add_argument("-i", "--image", action="store_true", default=False,
                                help="Argument to select image files")

    """
    In this block user defines other parameters for parsing
    (safe delete and recursion limit for depth of search of files; source and destination path of copying)
    """

    parser.add_argument("-c", "--count", type=int, default=50,
                        help="this is a counter of the depth of search in folder tree (Default is 50)")
    parser.add_argument("-s", "--safe_delete", action="store_true", default=False,
                        help="default is False")
    parser.add_argument("-f", "--formatting", action="store_true", default=False,
                        help="Sorting of files in destination folder (default is True)")
    parser.add_argument("-dp", "--destination", type=str,
                        default=os.path.abspath(os.curdir) + "\\destination\\",
                        help="type into your destination path (default is current dir + 'destination' dir")
    parser.add_argument("-sp", "--source_path", type=str,
                        default=os.path.abspath(os.curdir) + "\\content\\",
                        help="type into your source path(default is current dir + 'content' dir'")


    def get_arguments():
        args = vars(parser.parse_args())
        return args
