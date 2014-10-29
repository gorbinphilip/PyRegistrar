class Export(object):

    def __init__(self):
        pass

    def export(self, data_list, file_name):
        file=open(file_name, "w")
        for k, v in data_list:
            file.write(k+"\t:->\t"+v)
        file.close()
