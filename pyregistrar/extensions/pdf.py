from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ..exceptions import ExtensionError

class Export(object):
    """
    class for extension with export method to generate document
    """
    def __init__(self):
        pass

    def export(self, data_list, file_name):
        """
        method which export iterable data in data_list to pdf file of file_name
        """
        try:
            my_canvas = canvas.Canvas(file_name, pagesize=letter)
            my_canvas.setLineWidth(.3)
            my_canvas.setFont('Helvetica', 12)
            my_canvas.drawString(250, 750, "Registration Details")
            x=30
            y=720
            for k, v in data_list:
                my_canvas.drawString(x, y, k+"       : "+v)
                y=y-20
            my_canvas.save()
        except Exception:
            raise ExtensionError("unable to generate pdf")

