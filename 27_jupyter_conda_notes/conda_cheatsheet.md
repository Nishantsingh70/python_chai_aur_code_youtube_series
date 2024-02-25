# conda cheatsheet

### Important Note: If you want to deactivate an base environment permanently when we start a new command shell.

```bash
conda config --set auto_activate_base false
```

## Checking the number of environment
```bash
conda env list
```

## Create a new environment
```bash
conda create --name myenv python=3.6
```

## Activate an environment

```bash
conda activate myenv
```

## Deactivate an environment

```bash
conda deactivate
```

## Delete an environment

```bash
conda remove --name myenv --all
```

## Install a package

```bash
conda install --name myenv numpy
```

## List all packages installed in an environment

```bash
conda list --name myenv
```

## List all environments

```bash
conda info --envs
```

## To check the available option in conda

```bash
conda --help
```
