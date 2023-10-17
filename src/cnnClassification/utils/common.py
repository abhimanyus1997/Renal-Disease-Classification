# Standard library imports
import os  # Operating system-related functionalities
import yaml  # YAML data parsing
import json  # JSON data handling
import joblib  # Job serialization (typically used for saving/loading machine learning models)
from pathlib import Path  # Working with file paths
from typing import Any, List, Optional  # Type hints
import numpy as np
from PIL import Image

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

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data to a file using Joblib.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data from a file using Joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes (KB).

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in kilobytes (KB) as a string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring: str, fileName: str) -> None:
    """
    Decode a base64-encoded image string and save it to a file.

    Args:
        imgstring (str): Base64-encoded image string.
        fileName (str): Name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath: str) -> Optional[str]:
    """
    Encode an image from a file into base64 format.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        Optional[str]: Base64-encoded image as a string or None if the file doesn't exist.
    """
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except FileNotFoundError:
        return None


@ensure_annotations
def load_image(path: str, target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Load and resize an image from a file.

    Args:
        path (str): Path to the image file.
        target_size (Tuple[int, int]): The target size to which the image should be resized.

    Returns:
        np.ndarray: The image as a NumPy array.
    """
    image = Image.open(path)
    image = image.resize(target_size)
    return np.array(image)

@ensure_annotations
def batch_load_images(image_paths: List[str], target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Load a batch of images.

    Args:
        image_paths (List[str]): List of paths to image files.
        target_size (Tuple[int, int]): The target size for the images.

    Returns:
        np.ndarray: An array of loaded images.
    """
    images = [load_image(path, target_size) for path in image_paths]
    return np.array(images)

@ensure_annotations
def one_hot_encode(labels: List[int], num_classes: int) -> np.ndarray:
    """
    One-hot encode a list of class labels.

    Args:
        labels (List[int]): List of class labels.
        num_classes (int): Number of unique classes.

    Returns:
        np.ndarray: One-hot encoded labels.
    """
    return np.eye(num_classes)[labels]

@ensure_annotations
def split_dataset(dataset: List, split_ratio: float = 0.8) -> Tuple[List, List]:
    """
    Split a dataset into training and validation sets.

    Args:
        dataset (List): List of data points.
        split_ratio (float): Ratio of the dataset to be used for training.

    Returns:
        Tuple: Two lists - (training_data, validation_data).
    """
    split_index = int(len(dataset) * split_ratio)
    training_data = dataset[:split_index]
    validation_data = dataset[split_index:]
    return training_data, validation_data