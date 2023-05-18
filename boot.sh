# !/bin/sh
source venv/bin/activate
flask depoly
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - flasky:app