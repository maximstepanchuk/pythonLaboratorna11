import re
import zipfile
import io
import os


class FileManager:
    """Class that works with files"""

    @staticmethod
    def manage_zip(location: str, filename: str):
        """Prints all string that match regex from txt in zip"""
        regex = r'205\.189\.154\.54.*01/Jul/1995.*\.txt.*" 200'
        count = 0
        with zipfile.ZipFile(location) as zf:
            with io.TextIOWrapper(zf.open(filename), encoding="locale") as file:
                lines = file.readlines()
                for line in lines:
                    find_regex = re.search(regex, line)
                    if find_regex is not None:
                        print(find_regex.group())
                        count += 1
            print(f"Count of matches: {count}")

def main():
    file_name = "access_log_Jul95"
    # location = os.path.abspath(file_name)
    # FileManager.print_edu_bug(location=location)

    zip_name = "access_log_Jul95.zip"
    location = os.path.abspath(zip_name)
    FileManager.manage_zip(location=location, filename=file_name)
if __name__ == "__main__":
    main()