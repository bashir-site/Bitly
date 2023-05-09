# Bitly URL shortener

Bitly URL shortener is a Python script for dealing with bitly web links. The program shortens the link and checks whether it is bitlink, as well as displays the number of hits on this link.

## Installation

First of all you need to download all the files in this repo to your computer. Then you need to create and run a virtual environment with these commands:

On Mac OS and Linux:
```bash
# create environment with name venv
virtualenv venv -p python3
# runing venv enviroment
source venv/bin/activate
```

On Windows:
```bash
# create environment with name env
python -m venv env
# runing env enviroment
env\Scripts\activate
```

The next step is to install the necessary modules. This command will help:
```bash
pip install -r requirements.txt
```


## Usage

To use this script, you need to run it with a link to the site to check. For example the link to the site https://www.google.com/ can be checked with this command:

```bash
python main.py https://www.google.com/
```

The output should be like this:
"Количество переходов по ссылке битли: number"
Where number is the amount of time users have clicked this link


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Project Goals
This code was written for educational purposes as part of an online course for web developers at dvmn.org.

## Contacts

You can find my on telegram: https://t.me/bashir_77