**If the sign in modal is not opening, refresh your browser's cache**

## Installation guide

1. Clone this repository to your local machine

2. Navigate to the project root

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Populate database with seed data:

   ```bash
   python manage.py seed
   ```
   This creates the following accounts for testing purposes:

   ```bash
   username: `ricky`
   password: `SunnyvaleKing2025`
   ---------------------
   username: `bubbles`
   password: `KittyLord99`
   ```
   
5. Run the application and you're ready to go:

   ```bash
   python manage.py runserver
   ```

