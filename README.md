# Bigiron chatbot

A streamlit application that uses the langchain package to create a chat interface using large language models and a database.
The application uses Langchain to create an easy-to-use chat interface for users to retrieve Bigiron data efficiently and accurately. It connects to a PostgresSQL Database and uses various langchain classes to retrieve information from the same.

Steps:

1. Install required dependencies to run the model

   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables 1. Create a ‘.env’ file in the project directory 2. Add the line
   ```
   KEY=<YOUR_API_KEY>where <YOUR_API_KEY>
   ```
   is replaced with your OpenAI API key
3. Run the application
   ```
   streamlit run main.py
   ```
