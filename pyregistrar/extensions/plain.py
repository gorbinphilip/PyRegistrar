from ..exceptions import ExtensionError

class Export(object):
    """
    class for extension with export method to generate document.
    """
    def __init__(self):
        pass

    def export(self, data_list, file_name):
        """
        method which export iterable data in data_list to plain text file of file_name.
        """
        try:
            file=open(file_name, "w")
        except Exception:
            raise ExtensionError("unable to create file")
        try:
            for k, v in data_list:
                file.write(k+"\t\t: "+v+"\n")
        except Exception:
            raise ExtensionError("non iterable data_list")
        file.close()
