import os 
from pathlib import Path


project = "US-Visa"

files = [
    f"{project}/__init__.py",
    f"{project}/components/__init__.py",
    f"{project}/components/data_ingestation.py",
    f"{project}/components/data_validation.py",    
    f"{project}/components/data_transformation.py",
    f"{project}/components/model_trainer.py",
    f"{project}/components/model_evaluation.py",
    f"{project}/components/model_pusher.py",  
    f"{project}/configration/__init__.py",
    f"{project}/constants/__init__.py",    
    f"{project}/entity/__init__.py",
    f"{project}/entity/config__entity.py",
    f"{project}/entity/artifact__entity.py",        
    f"{project}/exception/__init__.py",    
    f"{project}/logger/__init__.py",        
    f"{project}/pipeline/__init__.py",
    f"{project}/pipeline/training__pipeline.py",
    f"{project}/pipeline/prediction__pipeline.py",
    f"{project}/utils/__init__.py",
    f"{project}/utils/main_utils.py",   
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"

]

# to prevent the path issue , it's differ in mac and windows  / or \
for filepath in files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,  exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"file is already present at :{filepath}") 
