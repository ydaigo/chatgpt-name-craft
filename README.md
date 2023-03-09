# chatgpt-name-craft

## 準備

.envファイルを作成

```.env
OPENAI_API_KEY=[APIキー]
```

## 通常の実行方法

```
pip install -r requirements.txt
```

```
python main.py
```

## Dockerでの実行方法

```
docker build . -t chatgpt-name-craft:0.0.1
```

```
docker run -p 7860:7860 chatgpt-name-craft:0.0.1
```
