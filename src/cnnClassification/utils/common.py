# Standard library imports
import os  # Operating system related functionalities
import yaml  # YAML data parsing
import json  # JSON data handling
import joblib  # Job serialization (typically used for saving/loading machine learning models)
from pathlib import Path  # Working with file paths
from typing import Any,  List, Optional  # Type hints

# Third-party library imports
from box.exceptions import BoxValueError  # BoxValueError exception from the box.exceptions module
from ensure import ensure_annotations  # ensure_annotations function from the ensure module
from box import ConfigBox  # ConfigBox class from the box module
import base64  # Encoding/decoding data in base64 format

# Custom module import (assuming this is a custom module)
from cnnClassification import logger  # Import the 'logger' module from the 'cnnClassification' package


@ensure_annotations
def read_yaml(yaml_file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        yaml_file_path (Path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox containing the parsed data from the YAML file.

    Raises:
        FileNotFoundError: If the specified YAML file does not exist.
        BoxValueError: If the loaded YAML is empty.
        yaml.YAMLError: If there is an issue with parsing the YAML file.

    Example:
        yaml_data = read_yaml(Path("config.yaml"))
        print(yaml_data.some_key)  # Access YAML data using dot notation.
    """
    try:
        with open(yaml_file_path, mode='r', encoding='utf-8') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)  # Use safe_load() to load YAML data safely
            if not yaml_data:
                raise BoxValueError("YAML is empty")  # Raise BoxValueError if YAML is empty
            logger.info(f"YAML file: {yaml_file_path} loaded successfully")
            return ConfigBox(yaml_data)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"YAML file not found: {yaml_file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")


@ensure_annotations
def create_directories(path_to_dirs: List[str], verbose: Optional[bool] = True):
    """
    Create a list of directories.

    Args:
        path_to_directories (List[str]): A list of directory paths to create.
        verbose (bool, optional): If True, log messages for created directories. Defaults to True.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save JSON data to a file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as file:
        content = json.load(file)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)
