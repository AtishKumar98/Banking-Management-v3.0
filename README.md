Banking Management Release Note (17-06-2022) - V3.0

Steps:

1. Clone Project:
   - Run the following command in Git Bash: `git clone https://github.com/AtishKumar98/Banking-Management`

2. Enable Scripts (if not already enabled) on your PC:
   - Run the following command in PowerShell as Administrator: `Set-ExecutionPolicy RemoteSigned -Scope LocalMachine`

3. Create Virtual Environment:
   - Run the following command in the VSCODE terminal where your project is located: `py -m venv VirtualEnv`

4. Activate Scripts from Virtual Environment:
   - Activate the scripts by running the command: `./VirtualEnv/Scripts/activate`

5. Go to the clone Directory/Folder:
   - Change the directory to the clone project using the command: `cd ./Banking-Management/`

6. Install Python Modules:
   - Install the required Python modules by running the command: `pip install -r requirements.txt`

7. Make migrations of Data, Tables, etc.:
   - Generate migrations using the command: `py manage.py makemigrations`
   - Apply the migrations using the command: `py manage.py migrate`

8. Enter into Python shell and add required data:
   - Launch the Python shell using the command: `python manage.py shell`
   - Execute the following commands to add necessary data:
     ```
     from django.contrib.auth.models import Group
     G = Group(id=1, name='Admin')
     G.save()
     from Product.models import ProductCode
     P = ProductCode(id=1, code=1101, name='SavingAc', maximum_withdrawal_amount=999999, annual_interest_rate=1.2, interest_calculation_per_year=1)
     P.save()
     ```

9. Create Superuser to login:
   - Run the command: `python manage.py createsuperuser`
   - Enter your username, email, password, and confirm the password as prompted

10. Run Development Server:
    - Finally, start the development server using the command: `python manage.py runserver`

Bugs and Fixes:

- Registration Error
- UI/UX of additional four
- Common Header/Navigation bar for all
- All links available in the navigation bar dropdown (Services)

Thanks & Regards,
Dev Team
Atish Kumar & Vyshali Lasitha
