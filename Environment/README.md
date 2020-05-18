##### Environment

In python, using the `pip` package manager, we can see the list of packages by running the following command.
```python
pip freeze

# below command will save the packages in a text file
pip freeze > requirements.txt

# we can import this text file to install those packages in a separate machine/environment
pip install -r requirements.txt
```

However, here, we will use `conda` as pakcage manager.
Let's say we're in `Anaconda prompt`:

```python
# creating a new conda environment that has the NumPy package
conda create -n test_env numpy

# activate the `conda` enviroment
conda activate test_env

# add `pandas` pacakge to the `test_env` enviroment
conda install pandas

# now we can use python shell to add some commands
>> e
>> import numpy as np

# exit the python shell in the virtual environment
exit()

# deactivate the virtual environment
conda deactivate
```

Sharing Environments between a conda Server and Your Local System:

```python
# activate the virtual env
conda activate test_env

# export the environemnt to a yml file
conda env export > test_env.yml

# deactivate and remove the environment from `conda`, so that we now no longer have the `test_env` environment
conda deactivate
conda env remove --name test_env

# recreate the `test_env` virtual environment by importing the yml file
conda env create -f test_env.yml 
```

###### _argparse_ to Accept Input from the User

```python
# Execute the file with no arguments supplied; the value of arguments.flag should be False:
python argparse_demo.py

# with the --flag argument, to set it to True:
python argparse_demo.py –-flag

# to see the help text:
python argparse_demo.py –-help
```

###### Positional arguments
The difference between a positional and a named argument is that a named argument starts with a hyphen (-), such as --flag, whereas, a positional argument does not start with a hyphen.

```python
python positional_args.py 
# throw error; the following arguments are required: source, dest, as it is using positional arguments

python positional_args.py A Z # Start from A to Z
```