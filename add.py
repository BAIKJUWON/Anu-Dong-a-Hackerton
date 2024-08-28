from flask import Flask, request, jsonify, render_template
import subprocess
import os
import tempfile

app = Flask(__name__)

"""
GPT 코드(보안상 제거)

"""
@app.route('/')
def home():
    """
    메인 페이지를 렌더링하는 엔드포인트
    """
    return render_template('index.html')

@app.route('/guide')
def guide():
    """
    가이드 페이지를 렌더링하는 엔드포인트
    """
    return render_template('Guide.html')

@app.route('/quiz')
def quiz():
    """
    퀴즈 페이지를 렌더링하는 엔드포인트
    """
    return render_template('Quiz.html')

@app.route('/code_runner')
def code_runner():
    """
    C 언어 코드를 입력하고 실행 결과를 확인하는 페이지를 렌더링하는 엔드포인트
    """
    return render_template('CodeRunner.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
