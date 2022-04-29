import urllib.request
import urllib.parse
from json import loads
url = "https://aerfaying.com/WebApi/Users/" + input("请输入用户id（无需“#”号）:") + "/Get"
data = {"key":"value"}
data = urllib.parse.urlencode(data)
data = data.encode()
response = urllib.request.urlopen(url=url,data=data)
data = response.read()
print(loads(data.decode())["user"]["abstract"])