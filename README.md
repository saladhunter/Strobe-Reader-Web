# Strobe Reader - Web Version

A fast, lightweight, open-source speed reading tool for the web.

## Features

✨ **Core Features:**
- Paste text and speed read it instantly
- Adjustable WPM (100-1500 words per minute)
- Real-time progress tracking
- No installation needed
- Zero user tracking
- Open source

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/saladhunter/Strobe-Reader-Web.git
cd Strobe-Reader-Web
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the app
```bash
python app.py
```

5. Open in browser
```
http://localhost:5000
```

## Usage

1. Paste text in the input box
2. Adjust WPM slider (default: 300 WPM)
3. Click "Start Reading"
4. Words appear one at a time - read at your own pace
5. Pause/resume anytime, or stop to try again

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Database**: None (stateless)

## Minimal Dependencies

This project intentionally keeps dependencies minimal:
- Flask only (12KB for this use case)
- No npm, webpack, or build tools
- No database required
- Works anywhere Python runs

## Project Structure

```
Strobe-Reader-Web/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend (all-in-one)
├── README.md
└── .gitignore
```

## Contributing

Contributions welcome! This is intentionally kept simple to be accessible to new contributors.

## License

MIT

## Related Projects

- [Strobe-Reader (Swift/macOS)](https://github.com/saladhunter/Strobe-Reader) - Native macOS version
