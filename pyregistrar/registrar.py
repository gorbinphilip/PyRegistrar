from . import console, models
import glob, os, importlib
from os.path import splitext, basename, abspath

__pkg__="pyregistrar"

def register(model, file_name, file_ext):
    """
    This method queries the user using console and creates the output file based on the params. The fields are automatically identified from models. It returns the file name on success.
    :model name of the model to be used(case sensitive and should be available in models)
    :file_name name for the output file
    :file_ext name of extension to used(case sensitive and should be available in extensions)
    """
    models=get_models()
    extensions=get_extensions()
    file_name=abspath(file_name)
    export_data=[]
    if models.__contains__(model) and extensions.__contains__(file_ext):
        real_model=load_class(model, "models", __pkg__)()
        real_extension=load_class("Export", file_ext, __pkg__+".extensions")()
        for field in real_model.get_list_fields():
            value=console.prompt(field)
            export_data.append((field.field_name, value))
            real_model.set(field.field_id, value)
        real_extension.export(export_data, file_name)
        return file_name
    else:
        raise Exception("unavailable models or extensions")


def get_models():
    """
    returns list of available models from models
    """
    return models.__all_models__


def get_extensions():
    """
    returns list of available output file formats from extensions
    """
    ext_dir=os.path.dirname(os.path.abspath(__file__))+"/extensions"
    extensions=find_modules(ext_dir)
    return extensions


def find_modules(directory):
    """
    returns list of names of modules in the directory excluding __init__.py file
    """
    modules=[]
    files = glob.glob("{}/*.py".format(directory))
    for file in files:
        if file.endswith("__init__.py"):
            continue
        else:
            name, ext = splitext(basename(file))
            modules.append(name)
    return modules

def load_class(name, module, package):
    """
    returns the class based on the params
    :name name of the class
    :module module name where the class is defined
    :package full package name to the module
    """
    mod=importlib.import_module("."+module, package)
    return getattr(mod, name)

def main(arg):
    """
    main method which can executed as script to run the registrar
    :arg should be the commandline params recieved by the script
    """
    models=get_models()
    exts=get_extensions()
    params=console.input_parser(models, exts, arg)
    print register(params[0],params[1],params[2])
