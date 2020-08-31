from flask import Flask, request, redirect, render_template
from app import app
from fastbook import *
from fastai.vision.widgets import *
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

learn_inf = load_learner('export.pkl', cpu=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload-image/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if allowed_file(image.filename):
                pred, pred_idx, probs = learn_inf.predict(PILImage.create(image))
                return render_template("public/upload_image.html", messages=f"Prediction: {pred}; Probability: {probs[pred_idx]:.04f}")
            else:
                return render_template("public/upload_image.html", messages=f"Sorry, invalid image type: Must be a: {ALLOWED_EXTENSIONS}")

    return render_template("public/upload_image.html", messages="")


@app.route('/')
def go_to_upload():
    return redirect("/upload-image/", messages="")


if __name__ == '__main__':
    app.run()
