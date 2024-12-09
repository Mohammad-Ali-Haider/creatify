from flask import Flask, render_template, request, redirect, url_for
import torch
from diffusers import DiffusionPipeline

app = Flask(__name__)

model_id = "CompVis/stable-diffusion-v1-4"
device = "mps" if torch.backends.mps.is_available() else "cpu"
pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "mps" else torch.float32)
pipe.to(device)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    with torch.no_grad():
        image = pipe(prompt, guidance_scale=8.5, num_inference_steps=50).images[0]
    image.save('static/generated_image.png')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
