import requests, json

teamName = 'TLJZ'
password = '123456' #security = no.1 priority
id = "33"
token = "VExKWjo6"

class Prvi:
	member1 = {'name':'Teo', 'surname':'KovacicKaramatic', 'mail':'tkovacick@tvz'}
	member2 = {'name':'Lovro', 'surname':'Samodol', 'mail':'lsamodol@tvz'}
	member3 = {'name':'Anto', 'surname':'Julardzija', 'mail':'ajulardz1@tvz'}
	member4 = {'name':'Domagoj', 'surname':'Zivanovic', 'mail':'dzivanovi@tvz'}
	
	members = [member1, member2, member3, member4]
	
	def execute(self):
		URL = "http://52.233.158.172/change/api/hr/account/register"
		headers = {'content-type':'application/json'}
		payload = {'Teamname':teamName, 'Password':password, 'Members':self.members}
		
		r = requests.post(URL, data=json.dumps(payload), headers = headers)
		
		print(r.text);
		
class Drugi:
	def execute(self):
		URL = "http://52.233.158.172/change/api/hr/account/login"
		headers = {'content-type':'application/json'}
		payload = {'Teamname':teamName, 'Password':password}

		r = requests.post(URL, data=json.dumps(payload), headers = headers)
		
		print(r.text);
		
class Treci:
	def execute(self):
		URL = "http://52.233.158.172/change/api/hr/team/details/" + id
		headers = {'X-Authorization' : token, 'content-type':'application/json'}
		
		r = requests.get(URL, headers = headers)
		print(r.text);

class Cetvrti:
	repo = "https://github.com/teokk1/ChangeCodeTLJZ"
	def execute(self):
		URL = "http://52.233.158.172/change/api/hr/team/confirm?id=" + id + "&repository=" + self.repo;
		headers = {'X-Authorization' : token, 'content-type':'application/json'}
		
		r = requests.get(URL, headers = headers)
		print(r.text);

	
Prvi().execute();
Drugi().execute();
Treci().execute();
Cetvrti().execute();