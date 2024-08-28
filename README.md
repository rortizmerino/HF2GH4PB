# HF2GH4PB

**Purpose**

This repository provides an example of a software project compliant with the [FAIR principles.](https://fair-software.nl/). It also adopts the recommendations made by the [TU Delft Guidelines on Research Software](https://d2k0ddhflgrk1i.cloudfront.net/TUDelft/Over_TU_Delft/Strategie/TU%20Delft%20Research%20Software%20Guidelines.pdf).

This repository includes documentation and examples on how to use HuggingFace pull requests to oepn issues in GitHub to be then posted into a project board.

## Installation

Following instructions have been developed on a computer running Windows 10 and wsl2

**Requirements** 
- Windows 10
- wsl2
- python 3

### Local installation

1. Install dependencies

Create environment
```bash
python3 -m venv .venv
```

Load environment
```bash
source .venv/bin/activate
```

Full installation from requirements
```bash
sudo apt-get install gh
python3 -m pip install -r requirements.txt
```

Step-wise installation
```bash
python -m pip install huggingface_hub
python -m pip install requests
```

Reminder in case more packages are installed
```bash
python3 -m pip freeze > requirements.txt
```

Initialize environment
```bash
source .venv/bin/activate
```

2. Set up access tokens

HuggingFace access token

```bash
cp set_HF_TOKEN_example.sh set_HF_TOKEN.sh
# modify set_HF_TOKEN.sh to include your token
# file is (and/or should be) included in .gitignore for security reasons
source set_HF_TOKEN.sh
```

GitHub access token

```bash
cp set_GH_TOKEN_example.sh set_GH_TOKEN.sh
# modify set_GH_TOKEN.sh to include your token
# file is (and/or should be) included in .gitignore for security reasons
source set_GH_TOKEN.sh
```

3. Run

```bash
python3 getnsetGHissues.py
```

4. Quick run (only after completing steps 1-3 at least once)

```bash
source .venv/bin/activate
source set_HF_TOKEN.sh
source set_GH_TOKEN.sh
python3 getnsetGHissues.py
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[LICENSE](./LICENSE)
[WAIVER](./WAIVER)

## Copyright

&copy; (2024) Raúl Ortiz, Delft, The Netherlands. 


