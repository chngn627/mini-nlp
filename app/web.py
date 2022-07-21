from flask import Flask, render_template, request
from app.entity_extrtaction import entity_extraction

app = Flask(__name__)


@app.route('/')
def student():
   return render_template('input.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

      s = result['input_text']
      texts_entities = entity_extraction(s)

      return render_template('result.html',result = texts_entities)


if __name__ == '__main__':
   app.run(debug = True)