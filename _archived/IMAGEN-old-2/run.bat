call py --version
call py -m venv _venv
call _venv\Scripts\activate
call py -m pip install -U pip
call pip install -r requirements.txt
call py app.py
pause