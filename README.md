# text_classification_LSTM_degital_ocean
In this we will do Text classification using LSTM and deploy in degital ocean

### Create the virtual env
```commandline
conda create -p venv python==3.7 -y
```

### To install packages from setup.py
```commandline
pythoc setup.py install
```
setup Degital ocean
app
select github
select your repo
select the branch
check auto deploy
click on next
command: gunicorn --worker-tmp-dir /dev/shm app:app
build the gproject
