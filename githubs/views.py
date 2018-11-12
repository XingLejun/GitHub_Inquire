from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	import requests
	import json
	api_request = requests.get("https://api.github.com/users?since=0")
	api = json.loads(api_request.content)
	return render(request,'githubs/index.html',{'api':api})

def user(request):
	if request.method == 'POST':
		import requests
		import json
		user = request.POST['user']
		user_request = requests.get("https://api.github.com/users/" + user)
		username = json.loads(user_request.content)
		return render(request, 'githubs/user.html',{'user':user,'username':username})
	else:
		notfund = "请在搜索框中输入查询用户……"
		return render(request, 'githubs/user.html', {'notfund':notfund})
