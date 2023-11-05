# Renal Disease Classification

## Introduction

This submodule, "Renal Disease Classification," is a part of the larger [MedicalAIProjects](https://github.com/abhimanyus1997/MedicalAIProjects) repository. It focuses on the classification of renal diseases using machine learning and artificial intelligence techniques.

## Repository Contents

This submodule contains the following components:

### Data
Information about the dataset used for training and testing the renal disease classification model.

 - **Dataset Information**
   The dataset was collected from PACS (Picture archiving and communication system) from different hospitals in Dhaka, Bangladesh where patients were already diagnosed with having a kidney tumor, cyst, normal or stone findings. Both the Coronal and Axial cuts were selected from both contrast and non-contrast studies with protocol for the whole abdomen and urogram. The Dicom study was then carefully selected, one diagnosis at a time, and from those we created a batch of Dicom images of the region of interest for each radiological finding. Following that, author excluded each patient's information and meta data from the Dicom images and converted the Dicom images to a lossless jpg image format. After the conversion, each image finding was again verified by a radiologist and a medical technologist to reconfirm the correctness of the data.

   Author's created dataset contains 12,446 unique data within it in which the cyst contains 3,709, normal 5,077, stone 1,377, and tumor 2,283.

    - **Citation**:
   Kindly Cite if you are finding this helpful:

   Islam MN, Hasan M, Hossain M, Alam M, Rabiul G, Uddin MZ, Soylu A. Vision transformer and explainable transfer learning models for auto detection of kidney cyst, stone and tumor from CT-radiography. Scientific Reports. 2022 Jul 6;12(1):1-4.
   [Source on Kaggle](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone)

### Code
 The source code for the classification model, including Jupyter notebooks, Python scripts, and any relevant resources.

### Documentation
Additional documentation, including model evaluation results, project details, and any specific instructions for usage.

## How to Use

To use this submodule in your own project or to contribute to its development, you can follow these steps:

1. Clone the parent repository [MedicalAIProjects](https://github.com/abhimanyus1997/MedicalAIProjects) to your local machine.

2. Initialize and update the submodule by running the following commands:
```
git submodule init
git submodule update
```

3. Explore the contents of the "Renal Disease Classification" submodule within your local copy of the parent repository.

4. Refer to the submodule's specific README and documentation for more information on using and contributing to this project.

## Contributors

- [Abhimanyu Singh](https://linkedin.com/in/abhimanyus1997): Maintainer

## License

This submodule is available under the [MIT License](LICENSE), which requires proper attribution to the project lead and maintainer. Please review the license for usage and distribution terms.

## Issues and Support

If you encounter any issues or have questions related to this submodule, please open an issue on the main "MedicalAIProjects" repository.

## Workflows

Set up workflows for managing development and deployment tasks.

### Update Configuration Files

1. Update `config.yaml` with project-specific settings.
2. Optional: Create and update `secrets.yaml` for securely managing sensitive information.
3. Update `params.yaml` with data preprocessing and model hyperparameters.

### Code Components

1. Update the project's primary entity.
2. Modify the configuration manager in the `src` directory.
3. Update components and pipeline as necessary.

### Entry Point

1. Update the `main.py` file to incorporate changes in configuration, components, and pipeline.

### Data Version Control

1. Update the `dvc.yaml` file if using Data Version Control for data and model management.

### Web Application (Optional)

1. If your project includes a web application, update `app.py` to reflect changes in configuration and components.

---

**LICENSE**

The MIT License (MIT)

Copyright (c) 2023 Abhimanyu Singh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
