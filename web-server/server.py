from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return  render_template('index.html', title="Home")

@app.route('/<string:page_name>')
def html_page(page_name):
  return  render_template(page_name, title=page_name)

@app.route('/submit_form', methods=['POST'])
def submit_form():
  if request.method == 'POST':
    #transform to a dictionary
    data = request.form.to_dict()
    print(data)
    return redirect('/thank-you.html',)
  else:
    return 'Something wen\'t wrong.'
