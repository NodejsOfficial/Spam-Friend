import os
import proxy_req
import subprocess
from colorama import Fore
from itertools import cycle

os.system('cls')	

def main():
	with open('tokens.txt', 'r') as tokens_file:
		tokens = [line.rstrip('\n') for line in tokens_file]
		print('Load '+str(len(tokens)) + ' Token '+f'in {Fore.LIGHTBLACK_EX}(token.txt){Fore.RESET}')
	user_id = input('user id : ')
	for token in tokens:
		subprocess.Popen(f'python spam.py -token={token} -user_id={user_id} -proxy_processor={proxy_req.GetProxy()}', shell=True)

main()