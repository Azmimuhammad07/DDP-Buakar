@echo off
title Django Server - DDP-Buakar
cd D:\Kuliah\DDP\DDP-Buakar
echo Activating virtual environment...
call venv\Scripts\activate
cd projek_ddp
echo Running Django server...
python manage.py runserver
pause
