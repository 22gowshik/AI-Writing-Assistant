from flask import Flask, request, jsonify
from flask_cors import CORS  
import google.generativeai as genai

app = Flask(__name__)

CORS(app)


genai.configure(api_key="AIzaSyDjDO2DmpR3nefynI4YdsYrfMo7g3FPvfs")
model = genai.GenerativeModel("gemini-1.5-pro")  


history = []

@app.route('/generate', methods=['POST'])
def generate():
    try:
        
        data = request.get_json()

        if 'input' not in data:
            return jsonify({"error": "No input text provided"}), 400
        
        input_text = data['input']

        
        prompt = f"""
        You are a helpful AI assistant who is specialized in writing content. 
        Your main task is to help the user by assisting them in writing tasks.
        User input: {input_text}
        """

        
        response = model.generate_content(prompt)

        
        clean_text = response.text.replace("*", "").strip()

        
        history.append({"TOPIC": input_text, "OUTPUT": clean_text})

        
        return jsonify({"generated_text": clean_text})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500


@app.route('/grammar-checker', methods=['POST'])
def grammar_checker():  
    try:
        
        data = request.get_json()

        if 'input' not in data:
            return jsonify({"error": "No input text provided"}), 400
        
        input_text = data['input']

        
        prompt = f"""
        You are a grammar correction assistant. Your task is to correct any grammar mistakes in the given text. 
        Please return only the corrected version of the text.
        Text:  {input_text}
        """

        
        response = model.generate_content(prompt)

        
        clean_text = response.text.replace("*", "").strip()

        
        history.append({"TOPIC": input_text, "OUTPUT": clean_text})

        return jsonify({"generated_text": clean_text})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500
@app.route('/plagiarism-checker', methods=['POST'])
def plagiarism_generate():
    try:
        
        data = request.get_json()

        if 'input' not in data:
            return jsonify({"error": "No input text provided"}), 400
        
        input_text = data['input']

       
        prompt = f"""
        You are an advanced AI-plagiarism detection tool. Analyze the following text for similarity to known sources. 
        Estimate the plagiarism percentage of the input texts. 
        Provide the plagiarism percentage in the expected way
        Text:  {input_text}
        Output: _%
         """

        
        response = model.generate_content(prompt)

        
        clean_text = response.text.replace("*", "").strip()

        
        history.append({"TOPIC": input_text, "OUTPUT": clean_text})

        
        return jsonify({"generated_text": clean_text})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500
    
@app.route('/summarize', methods=['POST'])
def summarize_generate():
    try:
        
        data = request.get_json()

        if 'input' not in data:
            return jsonify({"error": "No input text provided"}), 400
        
        input_text = data['input']

       
        prompt = f"""
        You are an super summarizer help me to summarize the given text. 
        Text:  {input_text}
        Output: _%
         """

        
        response = model.generate_content(prompt)

        
        clean_text = response.text.replace("*", "").strip()

        
        history.append({"TOPIC": input_text, "OUTPUT": clean_text})

        return jsonify({"generated_text": clean_text})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500

@app.route('/Brainstroming', methods=['POST'])
def Brainstroming_generate():
    try:
      
        data = request.get_json()

        if 'input' not in data:
            return jsonify({"error": "No input text provided"}), 400
        
        input_text = data['input']

       
        prompt = f"""
        You are an Brainstroming assistant. Your task is to Brainstrom for the given text . 
        Text:  {input_text}
         """

       
        response = model.generate_content(prompt)

        
        clean_text = response.text.replace("*", "").replace("#", "").strip()
        formatted_output = clean_text.split("\n")

        
        history.append({"TOPIC": input_text, "OUTPUT": formatted_output})

       
        return jsonify({"generated_text": clean_text})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500

@app.route('/history', methods=['GET'])
def get_history():
    
    return jsonify(history)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)
