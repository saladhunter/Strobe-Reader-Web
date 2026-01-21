from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def split_text(text):
    """Split text into words, preserving punctuation info"""
    words = re.findall(r'\S+', text.strip())
    return words

def calculate_reading_time(word_count, wpm):
    """Calculate reading time in seconds"""
    if wpm == 0:
        return 0
    return (word_count / wpm) * 60

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_text():
    """Process text and return word data"""
    data = request.json
    text = data.get('text', '').strip()
    wpm = int(data.get('wpm', 300))
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    words = split_text(text)
    reading_time = calculate_reading_time(len(words), wpm)
    
    return jsonify({
        'words': words,
        'word_count': len(words),
        'wpm': wpm,
        'reading_time_seconds': reading_time,
        'reading_time_display': format_time(reading_time)
    })

def format_time(seconds):
    """Format seconds into readable time"""
    if seconds < 60:
        return f"{int(seconds)}s"
    minutes = int(seconds / 60)
    secs = int(seconds % 60)
    return f"{minutes}m {secs}s"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
