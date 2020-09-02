# bear_class

A simple example bear classifier using colab to create the model and flask to enable a web app.

Work in progress.

### Manual setup
Create a virtual environment and manually install each of these (in this order)
```bash
pip install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

pip install fastai
pip install flask
pip install pillow
pip install ipython
```

### Quick install using requirements.txt
Coming soon...

### Running the app
The below commands will run the server and will output a URL you can use to access it.
```bash
set FLASK_APP=views
flask run
```

