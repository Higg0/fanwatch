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
Steps to commit:
    git commit -am 'comment'
    git push
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