from flask import Flask, render_template, request
app = Flask(__name__)

story = "hi placeholder"

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/newChapter', methods=['POST', 'GET'])
def new_chapter():
    global story
    if request.method == 'POST':
        story = request.form['contents']
    return render_template('newChapter.html')

@app.route('/story')
def view_story():
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug = True)
