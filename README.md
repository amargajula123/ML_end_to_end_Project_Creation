## Start Machine Learning Project.

### Software and account Requirements.
Requirements

   1. [Gitjub Account](https://github.com)
   2. [Heroku Account](https://dashboard.heroku.com/login)
   3. [VS Code IDE](https://code.visualstudio.com/login)
   4. [GIT cli](https://git-scm.com/download)
   5. [GIT DOCUMENTATION](https:/git-scm.com/docs/gittutorial)
   

 Creating conda environment
 '''
 conda create -p <env_name> python==3.7 -y
 '''

'''
conda activate venv/
'''
OR
'''
conda activate venv
'''
'''
pip install -r requirements.txt
'''
To add all files to git
'''
git add .
'''
OR
'''
git add file name
'''


Note : to ignore file or folder from git we can write name of file/folder in .gitignore file

To check git status
'''
git status
'''
to check all version maitained by git
'''
git log
'''
To create version / commit all changes by git
'''
git commit -m "massg"
'''
To send version / changes to git
'''
git push origin main
'''
To check remote url
'''
git remote -v
'''

To setup ci/CD pipeline in heroku we need 3 informations

1. HEROKU_EMAIL     =amargajula123@gmail.com
2. HEROKU_API_KE    =a29a9e91-0513-45b5-900e-7df11025697f
3. HEROKU_APP_NAME  =my-regression-app

Build docker image
'''
 <imag_name>:<tagname> .
'''
> Note : Image name for docker must be lowercase



