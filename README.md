# fanwatch_prototype

Built in the Cloud9 IDE
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 

Pushed to GitHub
https://docs.c9.io/v1.0/docs/setting-up-github-workspace
http://stackoverflow.com/questions/7355277/how-to-push-to-github-from-cloud9

Steps to commit an updated file:
    git commit -am 'comment'
    git push
Steps to commit new files and folders (need files in them):
    git commit -m 'comment'
    git push
    https://help.github.com/articles/adding-a-file-to-a-repository-from-the-command-line/
Making a new branch:
    git branch name
Switching branches:
    git checkout name
Pushing whole new branch to GitHub:
    git push origin name
    https://help.github.com/articles/pushing-to-a-remote/



Heavily inspired from this great tutorial
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Install Flask just in case
sudo easy_install Flask

Install packages (don't think I need most of these, but want to match the tutorial in case)
sudo pip install flask
sudo pip install flask-login
sudo pip install flask-openid
sudo pip install flask-mail
sudo pip install flask-sqlalchemy
sudo pip install sqlalchemy-migrate
sudo pip install flask-whooshalchemy
sudo pip install flask-wtf
sudo pip install flask-babel
sudo pip install guess_language
sudo pip install flipflop
sudo pip install coverage

TEST SITE:
https://fanwatch-prototype-higg0.c9.io/

RUN:
    python run.py $IP:$PORT
    Make sure you are in the right dir (use dir, cd, cd .)

PYTHON VERSION:
    python -c "import sys; print(sys.version)"
    
SQLLITE3:
    open console: sqlite3 db.fanwatch
    quit console: .quit
    https://www.sqlite.org/cli.html
    http://www.sitepoint.com/getting-started-sqlite3-basic-commands/

DB DETAILS:
    Link: https://www.dropbox.com/s/n7mh7vs28x7v3hn/DB%20schemas.jpg?dl=0
    User Data [user_id, username, first_name, last_name]
    Event Data [event_id, user_id, venue_id, event_score]
        note, each row will have different events and users for each event
    Venue List [venue_id, venue_name, address, lat, lng, type, event_id]
        https://developers.google.com/maps/articles/phpsqlajax_v3