import os

import gradio as gr
import openai
from dotenv import load_dotenv

load_dotenv()

BASE_PROMPT = '''
{}で【{}】の{}を考えてください。50文字以内で答えて。
'''


def create_name(programming_language, target, identifier):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=BASE_PROMPT.format(programming_language,
                                                                  target,
                                                                  identifier),
                                        temperature=0,
                                        max_tokens=7)
    return response.choices[0].text.replace("\n", "")


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            inputs = [gr.Radio(label="プログラム言語を選択してください。",
                               choices=["Python", "JavaScript", "Java", "Go言語", "PHP", "Ruby", "C言語", "C++", "C#"],
                               value="Python"),
                      gr.Text(label="日本語で命名してほしい内容を書いてください。", value="商品番号"),
                      gr.Radio(label="識別子の種類を選択してください。", choices=["変数名", "関数名", "クラス名", "定数名"],
                               value="変数名"),
                      ]
        with gr.Column():
            btn = gr.Button("送信")
            outputs = gr.Text(label="命名結果")
    btn.click(fn=create_name, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    demo.launch(show_api=False, server_name="0.0.0.0")
