# Python Flask Application

## Setup and Run Locally

### Prerequisites

- Python 3.12

### Steps

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv test-backend
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```sh
     .\test-backend\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source test-backend/bin/activate
     ```

4. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Create a [`.env`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fmagadi%2Fprojects%2Ftest%2Fbackend%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A0%7D%7D%5D%2C%22701ceb81-0473-407d-aa9f-d8021e99d591%22%5D "Go to definition") file in the root directory and add the following variables:

   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=root
   MYSQL_DB=TEST
   MYSQL_PORT=3309
   ```

6. **Run the application:**

   ```sh
   python app.py
   ```

7. **Access the application:**

   Open your browser and navigate to `http://127.0.0.1:5000`.

### API Documentation

Swagger documentation is available at `http://127.0.0.1:5000/apidocs`.
