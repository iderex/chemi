## Run locally

### Method 1:

Run the shell script on a Mac/Linux...
```
$ bash run.sh
```

...or run the batch file on Windows...
```
$ start run.bat
```
...and refresh the page

### Method 2:

Create a virtualenv & activate it
```
$ python3 -m venv venv
$ . venv/bin/activate
```

On Windows:
```
$ py -3 -m venv venv
$ . venv/Scripts/activate

```
On Windows cmd:
```
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

Install requirements
```
$ pip install -r requirements.txt
```

Run
```
$ export FLASK_APP=bunshi
$ export FLASK_ENV=development
$ flask run
```

On Windows cmd:
```
> set FLASK_APP=bunshi
> set FLASK_ENV=development
> flask run
```

Open [localhost:5000](http://127.0.0.1:5000) in a browser
