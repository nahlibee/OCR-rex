import os
from flask import render_template, request, jsonify,redirect, flash, url_for,Response
from config import app,db
from models import Info
from werkzeug.utils import secure_filename
from algo1 import reader_front
import base64
import json

@app.route("/infos", methods=["GET"])
def get_infos():
    infos = Info.query.all()
    json_infos = list(map(lambda x: x.to_json(), infos))
    return jsonify({"infos": json_infos})


@app.route("/create_info", methods=["POST"])
def create_info():
    
            
        liste=reader_front('save_pic.jpg')
        name = liste[0]
        adress = liste[3]
        dob = liste[1]
        cin=liste[3]
        if not name or not adress or not dob:
            return (
                jsonify({"message": "You must include a name, adress and dob and x"}),
                400,
            )

        new_info = Info(name=name, adress=adress, dob=dob,cin=cin)
        try:
            db.session.add(new_info)
            db.session.commit()
        except Exception as e:
            return jsonify({"message": str(e)}), 400

        return jsonify({"message": "User created!"}), 201


@app.route("/update_info/<int:user_id>", methods=["PATCH"])
def update_info(user_id):
    info = Info.query.get(user_id)

    if not info:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    info.name = data.get("name", info.name)
    info.adress = data.get("adress", info.adress)
    info.dob = data.get("dob", info.dob)
    info.cin = data.get("Cin", info.cin)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200


@app.route("/delete_info/<int:user_id>", methods=["DELETE"])
def delete_info(user_id):
    info = Info.query.get(user_id)

    if not info:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(info)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200



    

    





@app.route('/uplaod-image', methods=['POST'])
def index():
    """
    POST route handler that accepts an image, manipulates it and returns a JSON containing a possibly different image with more fields
    """
    # Read image from request and write to server's file system
    data = request.files['file'] 
    data.save('save_pic.jpg')
    


    # Do something with the image e.g. transform, crop, scale, computer vision detection
    # some_function_you_want()

    # Return the original/manipulated image with more optional data as JSON
    #saved_img = open('save_pic.jpg', 'rb').read() # Read as binary
    #saved_img_b64 = base64.b64encode(saved_img).decode('utf-8') # UTF-8 can be converted to JSON
    #response = {}
    #response['data'] = saved_img_b64
    #response['more_fields'] = 'more data' # Can return values such as Machine Learning accuracy or precision
    
    # If only the image is required, you can use send_file instead
    # return send_file('save_pic.jpg', mimetype='image/jpg') 
    liste=reader_front(r'C:\Users\yahya\Desktop\OCR rex\save_pic.jpg')
    name = liste[0]
    adress = liste[1]
    dob = liste[2]
    cin=liste[3]
    

    new_info = Info(name=name, adress=adress, dob=dob,cin=cin)
    try:
        db.session.add(new_info)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201
    #return Response(json.dumps(response))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)




