from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Add your OpenAI API key here
client = OpenAI(api_key="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")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate_script", methods=["POST"])
def generate_script():

    data = request.get_json()
    prompt = data["prompt"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional film script writer."},
            {"role": "user", "content": f"Write a short film script about: {prompt}"}
        ]
    )

    script = response.choices[0].message.content

    return jsonify({"script": script})


if __name__ == "__main__":
    app.run(debug=True)