# quiz-app
Quiz app developed with Django that allows you to create quizzes and obtain a grade based on the answers to their questions.

Quizzes, along with their questions and answers, are stored in a SQLite database. There is no user authentication or per-user data stored.

## Running the app

1. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it.

2. Install the requirements:

    ```shell
    python3 -m pip install -r requirements.txt
    ```

3. Run the migrations:

   ```shell
   python3 manage.py migrate
   ```
   
4. Run the local server at port 8000:

   ```shell
   python3 manage.py runserver 8000
   ```

5. The server should now be running at `http://127.0.0.1:8000/`. Navigate to this URL and enjoy the quiz-app :).
