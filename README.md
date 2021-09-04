# OpenAI Codex completions docker server
Listening on selected port and returns code completions with selected language
### Direct requests
If you have openai api key, just use [direct](https://github.com/format37/codex_completions/blob/main/client/direct.ipynb) requests to openai.
### Docker server
If you have openai api key and don't want to share him to others, to share Codex completion, you can:   
1. Build this docker server:
```
git clone https://github.com/format37/codex_completions.git
cd codex_completions
./compose.sh
```
2. Send requests from client like in [example](https://github.com/format37/codex_completions/blob/main/client/docker.ipynb)
### openai api reference
[create completions](https://beta.openai.com/docs/api-reference/completions/create)
