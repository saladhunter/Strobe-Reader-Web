# 🚀 Strobe Reader - Web Version

**The primary, actively developed version of Strobe Reader.**

A fast, lightweight, open-source speed reading tool for the web. No installation, no complexity - just paste text and start reading faster.

**[🎯 Try it live now!](#getting-started)** | [💻 Contribute on GitHub](https://github.com/saladhunter/Strobe-Reader-Web) | [📱 Works everywhere](#features)

## Features

✨ **Why the web version:**
- ✅ **Works anywhere** - Windows, Mac, Linux, mobile, tablet
- ✅ **No installation** - Just open a URL
- ✅ **Paste & read** - Start immediately
- ✅ **Adjustable WPM** - 100-1500 words per minute
- ✅ **Open source** - Contribute easily
- ✅ **Zero tracking** - Your privacy matters
- ✅ **Free forever** - No ads, no paywalls

## Getting Started

### 🌐 Use the Live App (Easiest)

Visit the deployed web app (link will be added after deployment).

### 🏠 Run Locally

**Prerequisites:**
- Python 3.8+
- pip

**Installation:**

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

**We'd love your help!** This project is intentionally kept simple to be accessible to new contributors.

### Ways to Contribute

- 🐛 **Report bugs** - Open an issue
- ✨ **Suggest features** - Discuss in issues
- 🔧 **Submit code** - Fork, create a branch, submit PR
- 📚 **Improve docs** - Better guides and examples
- 🎨 **UI/UX improvements** - Make it beautiful

### Getting Started with Code Changes

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes
4. Test locally: `python app.py`
5. Commit with clear message: `git commit -m "feat: Add your feature"`
6. Push and create a Pull Request

**Minimal stack = Easy onboarding!** 🎉

## License

MIT - Free and open source

## Roadmap

- [x] Core OPRS speed reading
- [x] Web deployment
- [ ] Dark mode
- [ ] Import from files
- [ ] Reading history
- [ ] Different reading modes
- [ ] Mobile optimization

## Status

✅ **Active development** - Primary focus for speed reading tool

---

**Questions?** [Open an issue](https://github.com/saladhunter/Strobe-Reader-Web/issues) or start a discussion!
