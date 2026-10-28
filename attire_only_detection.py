import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from model import run_pipeline

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"message": "❌ No file part"})

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"message": "❌ No selected file"})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    try:
        output_imgs, summary, civilian_count = run_pipeline(file_path)

        detection_img_path = os.path.join("uploads", "detection.jpg")
        output_imgs["Personnel Detection"].save(detection_img_path)

        return jsonify({
            "message": "✅ Processed successfully",
            "summary": {
                "civilians": civilian_count
            },
            "detection_img": detection_img_path
        })

    except Exception as e:
        return jsonify({"message": f"❌ Error in pipeline: {str(e)}"})

if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(debug=True)
