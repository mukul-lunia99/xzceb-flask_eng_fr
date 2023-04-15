from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    FrenchText = translator.translateToFrench(textToTranslate)
    return FrenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    EnglishText = translator.translateToEnglish(textToTranslate)
    return EnglishText

@app.route("/")
def renderIndexPage(): 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
