# CST 205 Final Project
This is our final project for CST 205, which is a book recommendation app written in Python with Flask and requests. The app allows users to search for a book by title, author, or ISBN, and returns a list of books that are recommended by the [Big Book API](https://bigbookapi.com). The user can then click on a book to view more details about it, such as the author, publisher, and a brief description.

## Installation
1. Clone the repository by running `git clone https://github.com/zliel/CST205-Final-Project.git` in your terminal
2. Navigate to the project directory
3. Install the required packages by running `pip install -r requirements.txt`
4. Add a `.env` file to the project directory with the following contents:
```
API_KEY="API KEY HERE"
```
5. Run the app by running `flask --app main --debug run` if developing, or `flask --app main run` if running normally
6. Open the app in your browser by going to `http://127.0.0.1:5000`
