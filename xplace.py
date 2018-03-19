from twill.commands import *
import twill
import json
#import redis

agent("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")
go("https://www.xplace.com/il/")

formvalue ("3", "j_username", "****")
formvalue ("3", "j_password", "***")
formvalue ("3", "brtz", "Asia/Jerusalem")
submit  ("3")

save_cookies("cookies.txt")
go ("https://www.xplace.com/il/rec?searchResultsOnly=true")
save_cookies("cookies.txt")

clear_extra_headers()
add_extra_header( "user-agent", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
add_extra_header( "accept", 'application/json')

add_extra_header( "accept-language", 'en-US,en;q=0.9')

show_extra_headers()
show_cookies()
go ("https://www.xplace.com/il/rest/user/projects/search/recommend/0/10?usg=WEB_SITE&brtz=Asia%2FJerusalem&_=1521474282916")
html = twill.get_browser().get_html()
print(type(html))


json_obj = json.loads(html)

for job in json_obj["responsePayload"]["recommendedProjectsCollection"]:
	go ("https://www.xplace.com/il/rest/public/project_ext?projectId={}&usg=WEB_SITE&brtz=Asia%2FJerusalem".format(job["searchRecommendedProjectId"]))
	print("****project_ext*****")
	html = twill.get_browser().get_html()
	print(html)
	go ("https://www.xplace.com/il/rest/public/project_bids_ext?projectId={}&usg=WEB_SITE&brtz=Asia%2FJerusalem".format(job["searchRecommendedProjectId"]))
	print("****project_bids_ext*****")
	html = twill.get_browser().get_html()
	print(html)
	
