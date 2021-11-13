from httpx import AsyncClient
import argparse
import os
import time
import asyncio
import httpx


# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument('-token', default=False)
parser.add_argument('-user_id', default=False)
parser.add_argument('-proxy_processor', default=False)
args = parser.parse_args()
if not args.token: exit()
if not args.user_id: exit()
if not args.proxy_processor: exit()
async def rc(len):
	return os.urandom(len).hex()[len:]


async def send_fr(token, user_id):
	headers = {
		'authorization': token,
		'content-type': 'application/json',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
	}

	try:
			while True:
				time.sleep(1)
				res = await httpx.put(f'https://discord.com/api/v9/users/@me/relationships/{user_id}', headers=headers, json={}, timeout=100)
				return res

	except Exception as e:
		# print(e)
		pass


async def _send_fr(token, user_id, proxy):
		async with AsyncClient(proxies={'http://': 'https://'+ proxy}) as s:
			res = await send_fr(token, user_id)
			print(f'Send {token} to ',{user_id},'Success')
		# if res.status_code == (403,429):
		# 	print(f'[!] Rate limit')
		# else:
		# 	print(res.text)

		
async def main():
	await _send_fr(args.token, args.user_id, args.proxy_processor)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())