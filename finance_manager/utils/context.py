class FileContext:
    """
    Context manager for working with files
    """
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        if self.file:
            self.file.close()

