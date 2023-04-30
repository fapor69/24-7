# InVoice-24-7
Allows you to keep your account in voice channel 24/7.

Make sure to select main.py as the default entry point.

Run the commands below in shell in order:

pip uninstall -y -r <(pip freeze) # <()

pip install -r requirements.txt

Inside main.py...

You may edit line 13 to change your status. (eg. dnd, idle and Online)

You may edit line 16 to change the mute/deaf state. (To mute/deaf, replace False with True. To do the opposite, do the opposite.)


If you want to keep this running 24/7, copy the server link given on the right side and automate it using an uptime website. (eg. https://cron-job.org/)
