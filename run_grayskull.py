"""Touch up the conda recipe from grayskull using conda-souschef."""
from souschef.recipe import Recipe
import os
from os.path import join

import ElMD

name, version = ElMD.__name__, ElMD.__version__
# os.system("grayskull pypi {0}=={1}".format(name, version))
os.system("grayskull pypi https://github.com/sgbaird/ElMD.git")

fpath = join(name, "meta.yaml")
fpath2 = join("scratch", "meta.yaml")
my_recipe = Recipe(load_file=fpath)
my_recipe["requirements"]["host"].append("flit")
del my_recipe["test"]["imports"][0]
my_recipe["test"]["imports"].append("ElMD")

my_recipe.save(fpath)
my_recipe.save(fpath2)
