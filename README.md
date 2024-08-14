# Speech-to-Text and Translation

This project demonstrates a simple Python application that converts speech to text using the Google Speech Recognition API and then translates the text into a specified language using the Google Translate API.

## Features

- **Speech-to-Text**: Captures audio from the microphone and converts it into text.
- **Translation**: Translates the captured text into a specified language.

## Requirements

- Python 3.x
- `speech_recognition` library
- `googletrans` library
- `pyaudio` library (for audio input)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Kimmy-hub/TextToSpeechConverter-Translator.git
    cd TextToSpeechConverter-Translator
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install speech_recognition googletrans pyaudio
    ```

## Usage

1. **Run the script**:

    ```bash
    python script_name.py
    ```

2. **Speak into your microphone** when prompted.

3. **View the output**:
   - The original text will be printed.
   - The translated text will be displayed in the specified language (default is Hindi).

## Configuration

- **Default Language**: The default language for translation is Hindi (`'hello'`). You can change this by modifying the `dest_lang` parameter in the `translate_text` function.

## Troubleshooting

- If you encounter issues with audio input, ensure that your microphone is properly set up and accessible.
- For translation errors, verify that you have an active internet connection and that the Google Translate API is accessible.

## Author

Ankit Kumar  
(ant880423@gmail.com)  
(https://github.com/Kimmy-hub)

