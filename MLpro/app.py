import numpy as np
from flask import Flask, request, render_template
import caption


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        preprocessdata = caption.preprocess_image(path)
        myresult = caption.predict(preprocessdata)
        print(myresult)
    return render_template("result.html", result=myresult)


if __name__ == '__main__':
    app.run(debug=True)
