from maclookup import ApiClient
import json
import sys, os

api_key = os.environ['API_KEY']
client = ApiClient(api_key)
macData = json.loads(client.get_raw_data(sys.argv[1],"json"))

for key,val in macData.items():
	print "-------",  key, "-------"
	for skey,sval in val.items():
	    print skey, "=>", sval
