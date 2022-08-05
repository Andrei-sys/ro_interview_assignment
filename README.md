# ro_interview_assignment

Solution for SDN role proposal

## Local execution


### Prerequisites:
* Python3: `sudo apt-get install python3` / `brew install python3`
* virtualenv: `python3 -m pip install virtualenv`

### Setup:

NOTE: you have to be in the `ro_interview_assignment` directory
* Create a new virtual env: 
    * `virtualenv -p python3 virtualenv_interview`
    * `source virtualenv_interview/bin/activate`
* Install dependencies:
    * `python3 -m pip install -r requirements.txt`

### Run:

`python3 main.py`

### Unit Testing:

Import files is not working properly. If you still need to run it, move the `test.py` file in the `ro_interview_assignment` folder and run it as following:

`python3 test.py`
