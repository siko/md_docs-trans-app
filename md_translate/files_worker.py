from pathlib import Path
import shutil
from typing import TYPE_CHECKING, Iterable
import os


class TraversalFun():

    def __init__(self, original_dir, dist_dir="") -> None:
        self.original_dir = original_dir
        self.dist_dir = dist_dir
        self.md_files_list: list = []

    def traversal_dir(self) -> None:

        dirs, filename = os.path.split(self.original_dir)
        # print('dirs:', dirs)
        # print('filename=', filename)

        _dist_dir = ""
        if self.dist_dir == "":
            _dist_dir = os.path.abspath(os.path.join(
                dirs, filename))
        else:
            _dist_dir = self.dist_dir

        if not os.path.exists(_dist_dir):
            os.makedirs(_dist_dir)

        TraversalFun.all_files(self, self.original_dir, _dist_dir)

    def all_files(self, original_dir, dist_dir='') -> None:

        for lists in os.listdir(original_dir):
            path:Path = os.path.abspath(os.path.join(original_dir, lists))
            newpath:Path = os.path.abspath(os.path.join(dist_dir, lists))

            if os.path.isfile(path):
                # print('original path:', path)
                # print('dist path:', newpath)

                shutil.copy(path, newpath)
                filename, file_extension = os.path.splitext(path)

                if file_extension == '.mdx' or file_extension == '.md':
                    ppath = Path(newpath)
                    self.md_files_list.append(ppath)

            if os.path.isdir(path):
                # print('dist path:', newpath)
                if not os.path.exists(newpath):
                    os.mkdir(newpath)

                TraversalFun.all_files(self, path, newpath)

      
