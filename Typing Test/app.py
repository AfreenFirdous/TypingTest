from flask import Flask, render_template, request
from handler import Typing_Handler

app = Flask(__name__)

app.config['SECRET_KEY'] = 'uppsismysecret'

@app.route('/')
def home():
    content = Typing_Handler.display_home()
    return render_template('home.html', content=content, visibility='invisible')

@app.route('/', methods=['POST'])
def validate_content():
    if request.method == 'POST':
        input_content = request.form.get('content')
        total_entries, accurate_entries, total_errors, accuracy, wpm = Typing_Handler.get_typing_result(input_content)  
        return render_template('home.html', content=Typing_Handler._VALID_CONTENT, 
            visibility='visible', total_entries=total_entries,
            total_errors=total_errors, wpm=wpm, accuracy=accuracy,
            accurate_entries=accurate_entries
        )

if __name__ == '__main__':
    app.run(debug=True)
