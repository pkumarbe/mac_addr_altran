# mac_addr_altran
This below steps can be followed to get the MAC details...

1. Build the docker image-
	#docker build -t get_macaddr:0.0.1 .
2. Execute the docker with created image. I have considered the macaddres.io API key as an environment. -
	#docker run --env API_KEY="Your api key" get_macaddr:0.0.1 <MAC Address>
