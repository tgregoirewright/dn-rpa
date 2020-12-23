import os
import pathlib
import traceback
from typing import List


def find_pdfs(f: pathlib.Path, pdfs: List[pathlib.Path] = []) -> List[pathlib.Path]:
    """Search a folder hierarchy and return a list of PDFs.
    Symlinks are not searched.

    Parameters
    ----------
    f : str
        The path to the folder to search.

    pdfs : List[pathlib.Path]
        The list of found PDF paths.
    """
    try:
        for i in f.iterdir():
            if i.is_dir() and not i.is_symlink():
                find_pdfs(i, pdfs)
            elif i.suffix == ".pdf":
                pdfs.append(i)
    except AttributeError:
        print(
            ">>> The folder you're searching 'f' must be of type pathlib.Path."
        )
        traceback.print_exc()
    except Exception:
        traceback.print_exc()
    return pdfs


if __name__ == "__main__":
    search_folder = pathlib.Path("formats")
    pdfs = find_pdfs(search_folder)
    print(pdfs)
