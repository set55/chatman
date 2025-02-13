# AI Chat Bot

## Overview
his is a simple AI chat bot project that uses language detection and text-to-speech (TTS) to generate speech from mixed-language text.

## Project Structure
```
mchatman
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
├── requirements.txt
└── README.md
```

## Installation
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


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.