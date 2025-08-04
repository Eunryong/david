from flask import Flask, request, Response, render_template, jsonify
import os
import re
from io import BytesIO
from gtts import gTTS
import base64
from datetime import datetime

app = Flask(__name__)

VALID_LANGS = ["ko", "en", "ja", "es"]

def is_text_valid_for_lang(text: str, lang: str) -> bool:
    """언어별 텍스트 검증 함수 (간단한 정규식 기반)"""
    patterns = {
        "ko": r"^[가-힣\s\d\.,!?~]*$",   # 한글, 공백, 숫자, 일부 기호
        "en": r"^[a-zA-Z\s\d\.,!?~]*$", # 영어, 공백, 숫자, 일부 기호
        "ja": r"^[\u3040-\u30ff\u4e00-\u9faf\s\d\.,!?~]*$", # 일본어(히라가나, 가타카나, 한자)
        "es": r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s\d\.,!?~]*$"  # 스페인어(특수문자 포함)
    }
    return re.match(patterns.get(lang, r".*"), text) is not None

@app.route("/", methods=["GET", "POST"])
def post():
    if request.method == 'GET':
        return render_template('index.html', title="Flask Example", name="은룡")
    elif request.method == 'POST':
        try:
            text = request.form.get('input_text', '').strip()
            lang = request.form.get('lang', 'ko')

            if not text:
                raise ValueError("텍스트가 비어 있습니다.")
            if lang not in VALID_LANGS:
                raise ValueError(f"잘못된 언어 코드입니다. 허용: {', '.join(VALID_LANGS)}")
            if not is_text_valid_for_lang(text, lang):
                raise ValueError(f"입력된 텍스트가 선택한 언어({lang})와 일치하지 않습니다.")

            log_line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] lang={lang}, text={text}\n"
            with open("input_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(log_line)

            fp = BytesIO()
            tts = gTTS(text=text, lang=lang, tld="com")
            tts.write_to_fp(fp)
            fp.seek(0)
            
            audio_base64 = base64.b64encode(fp.getvalue()).decode("utf-8")

            image_url = os.path.join(app.root_path, "static", "david.jpg")
            with open(image_url, "rb") as f:
                image_base64 = base64.b64encode(f.read()).decode("utf-8")

            return render_template("index.html", audio=audio_base64, image=image_base64)

        except ValueError as ve:
            return render_template("index.html", error=str(ve)), 400

        except Exception as tts_error:
            return render_template("index.html", error=str(tts_error)), 500



if __name__ == '__main__':
    app.run('0.0.0.0', 8080)