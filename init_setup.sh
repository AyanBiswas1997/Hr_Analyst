echo [$(date)]: "Start"

echo [$(date)]: "creating env with python 3.8"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "activate the env"

source activate ./env

echo [$(date)]: "Installing the enviroments"

pip install -r requirements.txt

echo [$(date)]: "End"