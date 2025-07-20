[![MIT](https://img.shields.io/github/license/trgr-karasutoragara/PipCanSelfReliance)](https://github.com/trgr-karasutoragara/PipCanSelfReliance)
[![Stars](https://img.shields.io/github/stars/trgr-karasutoragara/PipCanSelfReliance?style=social)](https://github.com/trgr-karasutoragara/PipCanSelfReliance/stargazers)
![Last Commit](https://img.shields.io/github/last-commit/trgr-karasutoragara/PipCanSelfReliance)


<br>


# A System That Makes Python Handle Its Own pip Migration
Tired of pip commands? Here's a script to let you focus on what matters: your research.

## Introduction: Command-Free Python Environment Setup

I have developed a system that automatically installs all necessary libraries (tools) just by running a single Python script.
This is part of my research philosophy: "translate complexity and solve problems through structure."

## How to Use (Just 2 Steps)
### Step 1: Create a "Library List" from Your Old Environment (Optional)

If you want to replicate an existing Python environment, open a terminal in that environment and create a "library list" (requirements.txt / requirements_myenv.txt) with the following command.

#### For the global environment:
```
your-account@your-old-pc:~$ pip freeze > requirements_pip.txt
```

#### For a virtual environment:
```
## First, activate your virtual environment
$ source ~/myenv/bin/activate
(myenv) your-account@your-old-pc:~$ pip freeze > requirements_myenv.txt
```

### Step 2: Run the Script in Your New Environment
Just download and run [en-install_packages.py](https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/en-install_with_log.py).(The [jp-install_packages.py](https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/jp-install_with_log.py) is the Japanese version, which is why some sample logs are in Japanese).

**Windows**: Double-click en-install_packages.py or run python en-install_packages.py in your terminal.

**Mac/Linux**: Run python3 en-install_packages.py in your terminal.

If you need to install into a virtual environment on Linux, first enter the environment with source ~/myenv/bin/activate, and then run the Python script.

Inside the Python script, the line install_requirements("requirements_pip.txt") specifies which file to read. You can change this part of the script to use a different file if needed.

The installation will start automatically, and you will see the progress on your screen. When it's finished, a log file named pip_install.log will be created.

## Sample
https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/requirements.txt

https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/requirements_myenv.txt

https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/pip_install.log

https://github.com/trgr-karasutoragara/PipCanSelfReliance/blob/main/pip_install2.log

## What This Script Solves
No More Commands: You don't need to remember commands like pip install -r ....

Visible Progress: You can see exactly which library is being installed at a glance.

Automatic Error Logging: If a problem occurs, the log file makes it easy to identify the issue.

      ↓
      
I hope this gives you more time for your work!

## License

This system is provided under the MIT License. Please feel free to extend it to fit your needs.
