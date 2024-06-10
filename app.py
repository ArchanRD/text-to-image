from flask import Flask, render_template, request
from generateImage import generate_image, save_image
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", image_url='https://via.placeholder.com/600', prompt="")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    async def handle_request(prompt):
        image_bytes = await generate_image(prompt)  # Generate the image
        response = await save_image(image_bytes)  # Save the image
        return response
    
    data = request.form['prompt']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(handle_request(data))

    return render_template('home.html', image_url=f"http://127.0.0.1:5000/static/{result}.jpeg", prompt=data)

if __name__ == "main":
    app.run(debug=True)