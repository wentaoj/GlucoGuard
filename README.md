# GlucoGuard: Diabetes Risk Prediction Model

## Project Information
#### Author: Wentao Jiang, Hai Xi
#### Release Date: Apr.20, 2023
_Last Edit: Dec.28, 2023_

## Project Overview
**"GlucoGuard"** is a data-driven Machine Learning model designed to predict the risk of developing diabetes in its early stages. It assists healthcare professionals in diagnosis and management. The project uses Python and various libraries to analyze the UCI Machine Learning Repository's Diabetes Risk Prediction Dataset, employing three classification models: Logistic Regression, Linear Support Vector Machine (SVM), and Polynomial SVM classifiers. "GlucoGuard" serves as a tool to aid healthcare professionals in early diabetes diagnosis, contributing to proactive healthcare.
### Keywords:
Diabetes Risk Prediction, Logistic Regression, Support Vector Machines, Machine Learning.

## Dataset Overview
### Early Stage Diabetes Risk Prediction Dataset (2020)
**Source:** [UCI Machine Learning Repository](https://doi.org/10.24432/C5VG8H)
#### Description:
The Early Stage Diabetes Risk Prediction Dataset is a critical component of our project. It provides comprehensive signs and symptoms data essential for identifying early-stage diabetes in patients. This dataset is instrumental in training and validating our predictive models.
#### Key Details:
- **Dataset Source**: UCI Machine Learning Repository
- **DOI**: [10.24432/C5VG8H](https://doi.org/10.24432/C5VG8H)
- **Characteristics**: Multivariate
- **Number of Features**: 17
- **Presence of Missing Values**: Yes

## Features and Models
- **Preprocessing**: Data normalization, Outlier detection, and Feature encoding.
- **Models Employed**: Logistic Regression, Linear SVM, Polynomial SVM.
- **Evaluation Metrics**: Accuracy, Confusion Matrix, Classification Report, ROC Curve & AUC Score.
- **Validation Techniques**: Train-Test Split (Standard), Cross-Validation (cross_val_score), and KFold Cross-Validation.

## Development Environment
- **Python Version**: 3.11.5 [Clang 14.0.6 ] on darwin (macosx14.0).
- **Conda and Pip Versions**: conda 23.11.0, pip 23.3.1.
- **Libraries**: Scikit-Learn, Pandas, NumPy, etc. See [`requirements.txt`](./requirements.txt) for details.
- **Dataset Location**: Located under `./data/` directory as [diabetes_data_upload.csv](./data/diabetes_data_upload.csv).

## Installations & Usage
1. Clone this repository to your local machine.
2. Check your current Python version with `python --version`. If not installed, download it from [Python](https://www.python.org/downloads/).
3. Install the required dependencies by running `pip install -r requirements.txt` in the project directory.
4. For detailed project instructions and examples, refer to the included Jupyter notebook [`GlucoGuard.ipynb`](./GlucoGuard.ipynb).
### Project Demo:
Run the following command under the project root directory, or simply run Section 4 from the notebook.
See notebook for Models Training and Evaluation Details.
```bash
# make sure all dependencies are installed
$ pip install -r requirements.txt

# Run the demo script
$ python ./models/demo.py

# Follow the on-screen prompts. The script accepts various input formats:
# For binary questions: [y/n], [yes/no], [1/0]
# For gender: [Male/Female], [M/F], [m/f], [1/0]
# Example interaction:
> Enter age (integer): 50
> Enter Gender (M/F): M
> Enter Polyuria (y/n): y
> Enter Polydipsia (y/n): y
> Enter Sudden Weight Loss (y/n): n
> Enter Weakness (y/n): y
> Enter Polyphagia (y/n): Y
> Enter Genital Thrush (y/n): N
> Enter Visual Blurring (y/n): n
> Enter Itchy Skin (y/n): y
> Enter Irritability (y/n): y
> Enter Delayed Healing (y/n): n
> Enter Partial Paresis (y/n): y
> Enter Muscle Stiffness (y/n): y
> Enter Alopecia (y/n): y
> Enter Obesity (y/n): y

# The script will provide model predictions and then prompt [y/n] to quit:
> Do you want to quit? (y/n): y

# Models Prediction Results:
Logistic Regression: ['Positive']
Linear SVC: ['Positive']
Polynomial SVC: ['Positive']
```
## Copyright Info
- **Dataset Description**: 
  - [Early Stage Diabetes Risk Prediction Dataset (2020)](https://doi.org/10.24432/C5VG8H). UCI Machine Learning Repository. DOI:10.24432/C5VG8H.
- **Models Developed by**: 
  - &copy; 2023 Wentao Jiang, Hai Xi.
- **License**: 
  - This project is licensed under the [MIT License](./LICENSE). Full license text is available in the repository.
- **Acknowledgments**: 
  - Special thanks to the developers and maintainers of the Scikit-Learn, Pandas, NumPy libraries, and other tools used in this project.

## Appendix
### Project Directory Structure:
```bash
.
├── Diabetes_Predictor-Slides.pdf
├── GlucoGuard.ipynb
├── LICENSE
├── README.md
├── data
│   └── diabetes_data_upload.csv
├── models
│   ├── demo.py
│   ├── model_lin_svc.pkl
│   ├── model_lr.pkl
│   └── model_polyn_svc.pkl
└── requirements.txt

3 directories, 10 file
```

<br>
&copy; 2023. Wentao (Todd) Jiang
