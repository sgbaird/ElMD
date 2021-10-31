"""Touch up the conda recipe from grayskull using conda-souschef."""
from souschef.recipe import Recipe
import os
from os.path import join
import ElMD

name, version = ElMD.__name__, ElMD.__version__
os.system("grayskull pypi {0}=={1}".format(name, version))

fpath = join(name, "meta.yaml")
fpath2 = join("scratch", "meta.yaml")
my_recipe = Recipe(load_file=fpath)
my_recipe["requirements"]["host"].append("flit")

my_recipe.save(fpath)
my_recipe.save(fpath2)
