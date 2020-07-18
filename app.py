from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/favicon.ico')
# def blog():
#     return 'this is my blog'

# @app.route('/<string:page_name>')
# def html(page_name):
#     return render_template(page_name)

@app.route('/<string:page_name>')
def html(page_name):
    return render_template(page_name)

def write_data(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file1 = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database2.csv',mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', newline='', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_Form', methods=['POST', 'GET'])
def submit_Form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data(data)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return 'something is wrong!, please check it once'










if __name__ == '__main__':
    app.run()
