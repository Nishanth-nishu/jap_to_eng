# Japanese to English Translator using MBART

This project implements a **Japanese to English translator** using Facebook's **MBART (Multilingual BART)** large model. The application is built as a Flask web app, enabling users to input Japanese text and receive English translations. Leveraging MBART's many-to-many translation capabilities, the model is fine-tuned specifically for Japanese-English translations.

## Project Structure

- **`app.py`**: The main Flask application file that handles routing, user input, model interaction, and rendering the HTML template.
- **`templates/index.html`**: The HTML template for the user interface, including input/output text areas and a translation button.
- **`static/styles.css`**: The stylesheet for styling the web application.
- **`testing.py`**: A script demonstrating the translation model's usage with example Japanese sentences.
- **`training.py`**: (Currently empty) Reserved for code related to training the MBART model if custom training is added in the future. Currently, a pre-trained model is used.
- **`setup.py`**: (Currently empty) Placeholder for packaging scripts or dependency management.
- **`requirements.txt`**: (Currently empty) Intended to list the project's dependencies, such as Flask and the Transformers library.

## Features

### Web Interface
- A simple and intuitive user interface built with Flask, allowing easy text translation.

### MBART Model
- Utilizes Facebook's **MBART-large-50-many-to-many-mmt**, a high-performance, pre-trained multilingual model.

### Client-Side Interaction
- Translation functionality occurs client-side, leveraging JavaScript for a seamless experience. (Note: The implementation assumes a locally saved pre-trained model, eliminating the need for an API key.)

### Error Handling
- Basic error handling in `app.py` ensures exceptions during the translation process are logged and handled gracefully.

## Setup and Installation

1. **Install Dependencies**:
   Create a virtual environment and install necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download the Pre-Trained Model**:
   Ensure the pre-trained MBART model is saved at the path specified in `app.py`. If not, download it from the [Hugging Face saved Model](https://huggingface.co/Nishur/jap_to_eng/tree/main). 

3. **Run the Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open a web browser and navigate to:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. Enter Japanese text into the input field.
2. Click the **"Translate"** button.
3. View the translated English text in the output field.

## Testing

The `testing.py` file provides example code to test the model’s functionality. Run the script independently to verify:
```bash
python testing.py
```
This script demonstrates translations of sample Japanese sentences using the loaded model and tokenizer.

## Potential Improvements

### Deployment
- Deploy the application to a cloud platform such as **Google Cloud Run**, **AWS Elastic Beanstalk**, or **Heroku** to make it widely accessible.

### API Key Handling
- Implement secure handling of API keys, if needed for future enhancements or external services.

### Enhanced Error Handling
- Improve error feedback to users with more descriptive messages and intuitive UI responses.

### Model Selection
- Add functionality to allow users to select from multiple pre-trained translation models.

### Comprehensive Testing
- Develop extensive unit and integration tests to improve code quality, reliability, and robustness.

With these features and improvements, the project has significant potential for further development and real-world deployment.

