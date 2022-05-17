import os
import sys
import hashlib


class HashError(Exception):
    """Custom error to be raised when two hashes are not identical.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)


def _read_file(file_path: str, method: str):
    """Reads file.
    """
    with open(file_path, method) as f:
        reggie_bytes = f.read()

    return reggie_bytes


def file_hash(data_folder: str, filename: str) -> str:
    """Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    data_folder : str
        folder where files are stored
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    file_path = os.path.join(data_folder, filename)
    reggie_bytes = _read_file(file_path=file_path, method='rb')

    return hashlib.sha1(reggie_bytes).hexdigest()


def validate_data(data_directory: str) -> None:
    """Read ``hash_list.txt`` file in ``data_directory``, check hashes
    
    An example file ``data_hashes.txt`` is found in the baseline version
    of the repository template for your reference.

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``hash_list.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``hash_list.txt`` file.
    """
    elements_dir = os.listdir(data_directory)
    for element in elements_dir:
        if element[-4:] == '.txt':
            content = _read_file(os.path.join(data_directory, element), method='r')

    hashes = []
    files = []
    for line in content.splitlines():
        hashes.append(line.split()[0])
        files.append(line.split()[1])

    for file in files:
        hash = file_hash(data_directory.split('/')[0], file)
        if hash not in hashes:
            raise HashError(f'The hash computed by our hashing algorithm ({hash}) is not in the provided list of '
                            f'validated hashes.')


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
