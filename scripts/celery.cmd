REM @echo off

cd ..

call env\Scripts\activate
cd project\myshop
celery -A myshop worker -l info

