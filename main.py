from flask import g, Flask, render_template, request, send_file, redirect, session, jsonify
import os
import re
import sqlite3
import glob
import re
import base64
import html
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), "static/uploads")
DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def parse_multi_form(form):
    data = {}
    for url_k, v in form.lists():
        if ('' in v):
            continue
        v = v[0]

        ks = []
        while url_k:
            if '[' in url_k:
                k, r = url_k.split('[', 1)
                ks.append(k)
                if r[0] == ']':
                    ks.append('')
                url_k = r.replace(']', '', 1)
            else:
                ks.append(url_k)
                break
        sub_data = data
        for i, k in enumerate(ks):
            if k.isdigit():
                k = int(k)
            if i+1 < len(ks):
                if not isinstance(sub_data, dict):
                    break
                if k in sub_data:
                    sub_data = sub_data[k]
                else:
                    sub_data[k] = {}
                    sub_data = sub_data[k]
            else:
                if isinstance(sub_data, dict):
                    sub_data[k] = v

    return data

def fnIterCategories(aCategories, aNewCategories, aOpened, iLevel=0):
    for oCategory in aCategories:
        sID = oCategory[0]
        aQueryCategories = query_db('SELECT * FROM categories WHERE parent_id=?', (sID,))
        
        aIterCategories = []
        if (sID in aOpened) and aQueryCategories and len(aQueryCategories)>0:
            aIterCategories = fnIterCategories(aQueryCategories, aNewCategories, aOpened, iLevel+1)
        
        oCategory = list(oCategory)
        sSpace = ""
        if iLevel:
            sSpace = "&nbsp;"
        oCategory[1] = iLevel * "&nbsp;&nbsp;" + sSpace + oCategory[1]
        aNewCategories = aNewCategories + [oCategory] + aIterCategories
    
    print(">>", aNewCategories)
    return aNewCategories


@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.args.get('init_db', '')=='1'):
        print("=========================================================")
        print("INIT DB")
        init_db()
        print("=========================================================")
        return redirect("/")

    sBaseURL = request.url

    sSelGroup = request.args.get('sSelGroup', '')
    sSelCategory = request.args.get('sSelCategory', '')
    sSelImage = request.args.get('sSelImage', '')

    if ("action" in request.args):
        if request.args["action"]=="image_upload":
            pass
        if request.args["action"]=="category_add_to_group":
            pass
        if request.args["action"]=="category_remove_from_group":
            pass
        if request.args["action"]=="image_add_to_category":
            pass
        if request.args["action"]=="image_remove_from_category":
            pass

    aGroups = query_db('SELECT * FROM groups')

    # if sSelGroup=='':
    #     if len(aGroups)>0 and len(aGroups[0])>1:
    #         sSelGroup=aGroups[0][0]

    dForm = parse_multi_form(request.args)
    print(request.args)

    aOpenedCategories = dict()
    if dForm.get('c', '') != '':
        aOpenedCategories = dForm['c']
        print(aOpenedCategories)

    aCategories = query_db('SELECT * FROM categories WHERE group_id=? AND parent_id IS NULL', (sSelGroup, ))
    aCategories = fnIterCategories(aCategories, [], list(aOpenedCategories))

    aImages = query_db('SELECT * FROM images WHERE category_id=?', (sSelCategory,))

    return render_template('index.html', 
        sSelGroup=sSelGroup,
        sSelCategory=sSelCategory,
        sSelImage=sSelImage,
        aGroups=aGroups,
        aCategories=aCategories,
        aImages=aImages,
        aOpenedCategories=aOpenedCategories
    )

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        for file in uploaded_files:
            sPath = os.path.join(UPLOAD_PATH, file.filename)
            sFileName = os.path.basename(sPath)
            file.save(sPath)
            get_db().execute("INSERT INTO image (name, path) VALUES (?, ?)", (sFileName, sPath))
            get_db().commit()
