import os
import sys

import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import joblib
import json
import yaml
from src.AdultIncomePrediction.logging import logger
from src.AdultIncomePrediction.exception import CustomException
from pathlib import Path
from typing import Any
import base64
from ensure import ensure_annotations
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            contents = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(contents)
    except Exception as e:
        raise CustomException(e, sys)
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    create list of directories
    
    Args:
    
         path_to_directories (list): list of path of directories
         ignore_log (bool, optional): ignore dirs is to be created. Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def load_json(path_to_json:str) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path_to_json) as json_file:
        content = json.load(json_file)

    logger.info(f"json loaded successfully from: {path_to_json}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")



@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)

        with open(path, "wb") as file:
            pickle.dump(data, file)
            logger.info(f"binary file saved at: {path}")

    except Exception as e:
        raise CustomException(e, sys)

def load_bin(path: Path) -> Any:
    """
    load binary file
    :param path:
    :return:
    """
    try:
        with open(path, "rb") as file:
            data = pickle.load(file)

    except Exception as e:
        raise CustomException(e, sys)




@ensure_annotations
def get_size(path: Path) -> str:
    """
        Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb: round(os.path.getsize(path) / 1024, 2)
    return f"~{size_in_kb} KB"

