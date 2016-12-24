import os
import json
import tempfile
from flask import Flask, make_response, request, redirect, url_for, send_file, abort, render_template
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
from wand.image import Image

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)

SUPPORTED_TYPES = ('jpg', 'png')

class UnsupportedType(HTTPException):
    code = 400
    description = '<h1>Unsupported type given</h1>'

@app.route('/v1/image/convert', methods=['POST'])
def convert_file():
    to_type = request.form.get('to_type', 'jpg') 
    if to_type not in SUPPORTED_TYPES:
        raise UnsupportedType("Invalid type given({0}). Only {1} are supported".format(to_type, SUPPORTED_TYPES))
    filepath = request.files['file']
    img = convert_pdf(filepath)
    tfile = tempfile.SpooledTemporaryFile()
    img.format = to_type
    img.save(file=tfile)
    img.close()
    tfile.seek(0)
    return send_file(tfile, mimetype='image/{0}'.format(to_type))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/v1/swagger', methods=['GET'])
def swagger():
    content = render_template('swagger.json')
    resp = make_response(content)
    resp.headers['Content-type'] = 'application/json'
    return resp

@app.route('/v1/image/info', methods=['POST'])
def image_info():
    filepath = request.files['file']
    img = convert_pdf(filepath)
    info = {
      'depth': str(img.depth),
      'size': str(img.size),
      'resolution': str(img.resolution)
    }
    img.close()
    return json.dumps(info)

@app.route('/v1/image', methods=['GET'])
def convert_form():
    return '''
    <!doctype html>
    <title>Convert image format</title>
    <h1>Upload Image</h1>
    <form method=post enctype=multipart/form-data action='image/convert'>
      <p>
         Image to convert: <input type=file name=file><br>
         Format to convert to[jpg,png]: <input type=text name=to_type value=jpg><br>
         <input type=submit value=Convert>
      </p>
    </form>
    '''

def convert_pdf(filepath):
    '''
    Turn pdf into multi page image
    http://stackoverflow.com/questions/23706661/imagemagick-wand-save-pdf-pages-as-images
    '''
    pdf = Image(file=filepath)

    pages = len(pdf.sequence)

    image = Image(
        width=pdf.width,
        height=pdf.height * pages,
        depth=pdf.depth * 2,
        resolution=pdf.resolution * 2
    )

    for i in xrange(pages):
        image.composite(
            pdf.sequence[i],
            top=pdf.height * i,
            left=0
        )
    image.resize(
        width=pdf.width * 2,
        height=pdf.height * pages * 2
    )
    pdf.close()

    return image

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
