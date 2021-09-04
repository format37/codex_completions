import asyncio
from aiohttp import web
import os
import json
import openai

async def call_test(request):	
	content = "ok"	
	return web.Response(text=content,content_type="text/html")

async def call_completion(request):
	
	request_str = json.loads(str(await request.text()))
	request = json.loads(request_str)	
	openai.api_key = request['token'] if 'token' in request.keys() else os.environ.get('TOKEN', '')	
	# https://beta.openai.com/docs/api-reference/completions/create
	response = openai.Completion.create(
		engine = request['engine'],
		prompt = request['prompt'].replace('***','"""'),
		max_tokens = int(request['max_tokens']),
		temperature = int(request['temperature']),
		top_p = int(request['top_p']),
		n = int(request['n']),
		echo = bool(request['echo']),
		stop = request['stop'],
		presence_penalty = int(request['presence_penalty']),
		frequency_penalty = int(request['frequency_penalty']),
		best_of = int(request['best_of'])
		)
	return web.Response(text=str(response),content_type="text/html")

app = web.Application(client_max_size=1024**3)
app.router.add_route('GET', '/test', call_test)
app.router.add_post('/completion', call_completion)

web.run_app(
    app,
    port=os.environ.get('PORT', ''),
)
