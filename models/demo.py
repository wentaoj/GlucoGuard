import pickle
import numpy as np
import os

def Age_to_onehot(inLst, input):
    try:
        normalized_age = (int(input) - 16 )/ (90 - 16) * 1 + 0
    except ValueError as e:
        print(f"Note: {e}; using default value")
        normalized_age = 0.5
    inLst.extend([normalized_age])

def Bool_to_onehot(inLst, input):
    if input.lower() in ['yes', 'y', '1']:
        inLst.extend([1, 0])
    elif input.lower() in ['no', 'n', '0']:
        inLst.extend([0, 1])
    else:
        print("Note: Input pattern not recognized; using default value")
        inLst.extend([0, 1])

def Gender_to_onehot(inLst, input):
    if input.lower() in ['male', 'm', '1']:
        inLst.extend([1, 0])
    elif input.lower() in ['female', 'f', 0]:
        inLst.extend([0, 1])
    else:
        print("Note: Input pattern not recognized; using default value")
        inLst.extend([1, 0])

def models_demo(lr, lin_svc, polyn_svc):    
    questions = {
        "> Enter age (integer): ": Age_to_onehot,
        "> Enter Gender (M/F): ": Gender_to_onehot,
        "> Enter Polyuria (y/n): ": Bool_to_onehot,
        "> Enter Polydipsia (y/n): ": Bool_to_onehot,
        "> Enter Sudden Weight Loss (y/n): ": Bool_to_onehot,
        "> Enter Weakness (y/n): ": Bool_to_onehot,
        "> Enter Polyphagia (y/n): ": Bool_to_onehot,
        "> Enter Genital Thrush (y/n): ": Bool_to_onehot,
        "> Enter Visual Blurring (y/n): ": Bool_to_onehot,
        "> Enter Itchy Skin (y/n): ": Bool_to_onehot,
        "> Enter Irritability (y/n): ": Bool_to_onehot,
        "> Enter Delayed Healing (y/n): ": Bool_to_onehot,
        "> Enter Partial Paresis (y/n): ": Bool_to_onehot,
        "> Enter Muscle Stiffness (y/n): ": Bool_to_onehot,
        "> Enter Alopecia (y/n): ": Bool_to_onehot,
        "> Enter Obesity (y/n): ": Bool_to_onehot
    }

    while True:
        inputLst = []
        for question, func in questions.items():
            answer = input(question)
            func(inputLst, answer)
        quit = input("\n Do you want to quit? (y/n): ")

        # Predict your input!
        inputLst = np.array(inputLst, dtype=float).reshape(1, -1)
        models = {
            "Logistic Regression": lr,
            "Linear SVC": lin_svc,
            "Polynomial SVC": polyn_svc
        }

        print("\n# Models Prediction Results:")
        for name, model in models.items():
            print(f"{name}: {model.predict(inputLst)}")
        
        if quit.lower() in ['yes', 'y', '1']:
            print('\n')
            break
        elif quit.lower() not in ['no', 'n', '0']:
            print("\nAssuming you want to quit; exiting...")
            break
        else:
            print('\n')
            continue

if __name__ == '__main__':
    with open (os.path.join(os.path.dirname(__file__), "model_lr.pkl"), 'rb') as f:
        model_lr = pickle.load(f)

    with open (os.path.join(os.path.dirname(__file__), "model_lin_svc.pkl"), 'rb') as f:
        model_lin_svc = pickle.load(f)

    with open (os.path.join(os.path.dirname(__file__), "model_polyn_svc.pkl"), 'rb') as f:
        model_polyn_svc = pickle.load(f)

    models_demo(lr=model_lr, lin_svc=model_lin_svc, polyn_svc=model_polyn_svc)
