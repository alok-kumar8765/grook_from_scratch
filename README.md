# Audio Transcription using OpenAI Whisper

A simple Python script to transcribe audio files into text using OpenAI's Whisper model and save the output to a text file.

## Features

- Uses OpenAI's **Whisper** model for accurate speech recognition.
- Automatically transcribes audio (`.mp3` or other supported formats) to text.
- Saves the resulting transcript to `transcript.txt`.
- Prints the generated transcript directly to the console.

## Prerequisites

- **Python 3.8+**
- **FFmpeg**: Whisper requires `ffmpeg` to be installed on your system.
  - **macOS** (via Homebrew): `brew install ffmpeg`
  - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
  - **Windows** (via Chocolatey): `choco install ffmpeg`

## Installation

1. Clone or download this repository.
2. Install the `openai-whisper` package using `pip`:

```bash
pip install openai-whisper
```

*Note: Depending on your environment, PyTorch will be automatically installed as a dependency.*

## Usage

1. Place your audio file in the same directory as the script and rename it to `audio.mp3` (or update the `file` variable in the script to match your audio file's path).
2. Run the script:

```bash
python transcribe.py
```

3. Once finished, you will find:
   - The transcript displayed in your terminal/console.
   - A new file named `transcript.txt` containing the transcribed text.

## Code Overview

```python
import whisper

# Path to your input audio file
file = "audio.mp3"

# Load the desired Whisper model ('tiny', 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Transcribe the audio file
text = model.transcribe(file)["text"]

# Save the transcript to a text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Output the transcript to the console
print("\nTranscript:\n", text)
```

## Available Models

Whisper provides several model sizes depending on your requirements for speed and accuracy:

| Size | Parameters | Required VRAM | Relative Speed |
| :--- | :--- | :--- | :--- |
| `tiny` | 39 M | ~1 GB | ~32x |
| **`base`** | **74 M** | **~1 GB** | **~16x** |
| `small` | 244 M | ~2 GB | ~6x |
| `medium` | 769 M | ~5 GB | ~2x |
| `large` | 1550 M | ~10 GB | 1x |

To switch models, simply change `"base"` in `whisper.load_model("base")` to your desired size (e.g., `"small"` or `"medium"`).

## License

This project is open-source and available under the [MIT License](LICENSE).
