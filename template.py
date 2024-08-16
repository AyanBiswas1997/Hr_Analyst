import os
from pathlib import Path
import logging
package="Hr_Analyst"
list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package}/__init__.py",
    f"src/{package}/components/__init__.py",
    f"src/{package}/components/data_ingestion.py",
    f"src/{package}/components/data_transformation.py",
    f"src/{package}/components/model_trainer.py",
    f"src/{package}/pipelines/__init__.py",
    f"src/{package}/pipelines/trainting_pipeline.py",
    f"src/{package}/pipelines/prediction_pipeline.py",
    f"src/{package}/logger.py",
    f"src/{package}/exception.py",
    f"src/{package}/utiles/__init__.py",
    "notebooks/Researsh.ipynb",
    "notebooks/data/.gitkeep",
    "setup.py",
]
# Here i create a Directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling
