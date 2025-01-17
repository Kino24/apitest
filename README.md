# This project uses Python version 3.10.11

## Installed Libraries
You need to run these commands on the Raspberry Pi
```sh
python -m pip install --upgrade pip
pip install ultralytics
pip install pillow
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```
If you're using a PC then you need to install ** CUDA version 11.8 ** and install ** pyenv ** to make life easier

first run shell as administrator and then enter this command

```sh
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

now install python 3.10.11
``sh
pyenv install 3.10.11
```

wait for the download to finish and then do
```sh
pyenv global 3.10.11
```

and then install the following libraries

```sh
python -m pip install --upgrade pip
pip install ultralytics
pip install pillow
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

# List of installed libraries
To see the list of installed libraries, run the following command in your terminal:

```sh
pip freeze
```

This will output a list of all installed libraries along with their versions.

## Example

Here is an example of what the output might look like:

```
absl-py==2.1.0
albucore==0.0.23
albumentations==2.0.0
annotated-types==0.7.0
anyio==4.8.0
asttokens==3.0.0
certifi==2024.12.14
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
coloredlogs==15.0.1
contourpy==1.3.1
cycler==0.12.1
decorator==5.1.1
exceptiongroup==1.2.2
executing==2.1.0
fastapi==0.115.6
filelock==3.13.1
flatbuffers==24.12.23
fonttools==4.55.3
fsspec==2024.2.0
gitdb==4.0.12
GitPython==3.1.44
grpcio==1.69.0
h11==0.14.0
humanfriendly==10.0
idna==3.10
ipython==8.31.0
jedi==0.19.2
Jinja2==3.1.3
kiwisolver==1.4.8
Markdown==3.7
MarkupSafe==2.1.5
matplotlib==3.10.0
matplotlib-inline==0.1.7
mpmath==1.3.0
networkx==3.2.1
numpy==2.2.1
onnxruntime==1.20.1
opencv-python==4.10.0.84
opencv-python-headless==4.10.0.84
packaging==24.2
pandas==2.2.3
parso==0.8.4
pillow==11.1.0
prompt_toolkit==3.0.48
protobuf==5.29.3
psutil==6.1.1
pure_eval==0.2.3
py-cpuinfo==9.0.0
pycocotools==2.0.8
pydantic==2.10.5
pydantic_core==2.27.2
Pygments==2.19.1
pyparsing==3.2.1
pyreadline3==3.5.4
python-dateutil==2.9.0.post0
python-multipart==0.0.20
pytz==2024.2
PyYAML==6.0.2
requests==2.32.3
scipy==1.15.1
seaborn==0.13.2
simsimd==6.2.1
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
stack-data==0.6.3
starlette==0.41.3
stringzilla==3.11.3
sympy==1.13.1
tensorboard==2.18.0
tensorboard-data-server==0.7.2
thop==0.1.1.post2209072238
torch==2.5.1+cu118
torchaudio==2.5.1+cu118
torchvision==0.20.1+cu118
tqdm==4.67.1
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2024.2
ultralytics==8.3.61
ultralytics-thop==2.0.13
urllib3==2.3.0
uvicorn==0.34.0
wcwidth==0.2.13
Werkzeug==3.1.3
```

Make sure to keep this list updated as you add or remove libraries from your project.