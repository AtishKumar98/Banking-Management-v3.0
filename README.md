# Banking-Management-v3.0
Banking Management
Release Note (17-06-2022) - V3.0
Steps:
•	Step 1: Clone Project
•	Step 2: If Scripts is not enabled on your PC, Enable it.
•	Step 3: Create Virtual environment.
•	Step 4: Activate Scripts from Virtual environment.
•	Step 5: Go to the clone Directory/Folder.
•	Step 6: Install Python Modules.
•	Step 7: Make migrations of Data, Tables etc.
•	Step 8: Enter into python shell, and Add required data.
•	Step 9: Create Super to login.
•	Step 10: Run Development by run server command.

Bugs and Fixes:
1)	Registration Error.
2)	UI/UX of additional four.
3)	Common Header/Navigation bar for all.
4)	All link available at navigation bar drop down (Services).






Thanks & Regards Dev Team
Atish Kumar & Vyshali Lasitha.
*Clone Project*
///Run this command in Git Bash///
command >>>   git clone https://github.com/AtishKumar98/Banking-Management
////////////////////////////////////////////////////
* To enable scripts on your pc*
///////Run this command in PowerShell As Administrator////////
command >>>Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
///////////////////////////////////////////////////
///////Run this command in VSCODE- VSCODE-TERMINAL Where your Project is ////////
Create *Virtual Env*
py -m venv VirtualEnv
Activate Scripts
./VirtualEnv/Scripts/activate
Go to the Directory clone Project
>>> cd ./Banking-Management/
///////////////
**Install Modules of python**
pip install - r requirements.txt
///////////////
**Migrate**
>>>py manage.py makemigrations
>>>py manage.py migrate
///////////////


**Run Shell Enter Some Data **
>>>python manage.py shell
from django.contrib.auth.models import Group
G = Group(id=1 ,name ='Admin')
G.save()
from Product.models import ProductCode
P = ProductCode(id=1, code=1101, name=SavingAc,maximum_withdrawal_amount=999999,annual_interest_rate=1.2,interest_calculation_per_year=1)
P.save()
///////////////
**Createsuperuser for super user**.
>>>python manage.py createsuperuser
	-Enter your username
	-Enter Email
	-Enter Password
	-Confirm Password
///////////
**And finally run server**
>>>python manage.py runserver
///////////////////////////////////////////////////
