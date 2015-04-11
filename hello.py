from flask import Flask, render_template, request
app = Flask(__name__)

story = "hi placeholder"

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/newChapter')
def new_chapter():
    return render_template('newChapter.html')

@app.route('/newChapter', methods=['POST'])
def submit_story():
    story = request.form['contents']

@app.route('/story')
def view_story():
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug = True)
