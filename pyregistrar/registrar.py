from . import console, models
import glob, os, importlib
from os.path import splitext, basename, abspath

__pkg__="pyregistrar"

def register(model, file_name, file_ext):
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
    else:
        raise Exception()


def get_models():
    """returns list of available models"""
    return models.__all_models__


def get_extensions():
    """returns list of available output file formats"""
    ext_dir=os.path.dirname(os.path.abspath(__file__))+"/extensions"
    extensions=find_modules(ext_dir)
    return extensions


def find_modules(directory):
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
    mod=importlib.import_module("."+module, package)
    return getattr(mod, name)

def main(arg):
    models=get_models()
    exts=get_extensions()
    params=console.main(models, exts, arg)
    register(params[0],params[1],params[2])
