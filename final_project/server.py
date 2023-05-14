from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route('/englishToFrench')
def english_to_french():
    text = request.args.get('text')
    translated_text = translator.english_to_french(text)
    return translated_text

@app.route('/frenchToEnglish')
def french_to_english():
    text = request.args.get('text')
    translated_text = translator.french_to_english(text)
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
