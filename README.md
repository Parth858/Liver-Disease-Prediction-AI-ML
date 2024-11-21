
# Liver Disease Prediction Model
### This repository contains a machine learning model to predict the likelihood of liver disease based on health parameters. The model is trained using an SVM classifier and deployed using Streamlit for an interactive user interface.

## *Features*

The model uses the following features for prediction:

* age: Age of the individual.
* sex: Gender (Male/Female).
* albumin: Albumin level in blood.
* alkaline_phosphatase: Level of Alkaline Phosphatase enzyme.
* alanine_aminotransferase: Level of Alanine Aminotransferase enzyme.
* aspartate_aminotransferase: Level of Aspartate Aminotransferase enzyme.
* bilirubin: Bilirubin level in blood.
* cholinesterase: Level of Cholinesterase enzyme.
* cholesterol: Cholesterol level in blood.
* creatinina: Creatinine level in blood.
* gamma_glutamyl_transferase: Level of Gamma-Glutamyl Transferase enzyme.
* protein: Total protein level in blood.
 
## *Repository Structure*

├── scaler.pkl                     :- _Scaler object for data preprocessing_

├── svm_liver_disease_model.pkl    :- _Trained SVM model_

├── Liver Disease Prediction.ipynb :- _Jupyter notebook for model training_

├── app.py                         :- _Streamlit app for deployment_

├── README.md                      :- _Project documentation_


## *Model Overview*

### *Training* : *The model was trained using the following steps*

1. Preprocessing:
    
    1. Handling missing values
    2. Encoding categorical variables
    3. Feature scaling

2. Model:

    1. Support Vector Machine (SVM) with a linear kernel.  
    
### *Performance* : The model achieved 93.6% accuracy on the test dataset.


## *File Details*

1. **Liver Disease Prediction.ipynb**: Contains the code for preprocessing, training, and evaluation.
2. **scaler.pkl**: Saved Scikit-learn StandardScaler object for input scaling.
3. **svm_liver_disease_model.pkl**: Trained SVM model for predictions.
4. **app.py**: Streamlit code for deploying the model as a web app.

Find the Model URL here: https://parth858-liver-disease-prediction-model.streamlit.app/





