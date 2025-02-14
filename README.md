# AI Chat Bot

## Overview
This is a simple AI chat bot project that uses language detection and text-to-speech (TTS) to generate speech from mixed-language text.

## Project Structure
```
chatman
├── config
│   ├── system.json.example
├── src
│   ├── main.py
|   ├── qt-input.py
|   ├── repeatSpeak.py
│   └── utils
│       ├── __init__.py
│       ├── listenbot.py
│       ├── qtui.py
│       ├── speakbot.py
│       └── thinker.py
├── tmp
├── requirements.txt
└── README.md
```

## Installation
This project requires Python 3.12. Ensure you have Python 3.12 installed on your system before proceeding.

To set up the project, clone the repository and navigate to the project directory. Then, install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage
To run the application and generate a .wav file named `output.wav` in the project's root directory, execute the following command:

```
python src/main.py
```

This will imitate the voice from `output.wav`.


If you want to use a Qt interface to input text and interact with the chat bot, use the following command:

```
python src/qt-input.py
```

If you just want the chat bot to repeat what you talk about (without running the LLM), use the following command:

```
python src/repeat-speak.py
```

## Configure chatbot character or other function
To configure the project, copy the `system.json.example` file to `system.json` in the `config` directory. You can use the content from the example file as a starting point and modify it as needed:

```
cp config/system.json.example config/system.json
```

Feel free to add any additional configurations or settings to the `system.json` file to suit your needs.

```
{
    "system_init": [
        {
            "role": "system",
            "content": "You are a AI agent"
        }
      ]
}
```

## Bot memory
To enable the chat bot to remember previous interactions, the bot's memory will be saved to `tmp/history.json`. If you wish to reset the bot's memory, simply delete this file:

```
rm tmp/history.json
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.