# mac_addr_altran
# Code used python
This below steps can be followed to get the MAC details...

1. Build the docker image-
	#docker build -t get_macaddr:0.0.1 .

2. Execute the docker with created image. I have considered the macaddres.io API key as an environment and provide the MAC address as an argument. -
<<<<<<< HEAD
	#docker run --env API_KEY="Your api key" get_macaddr:0.0.1 <MAC Address>


Ex- 
# docker run --env API_KEY="xxxxxxxxxx" get_macaddr:0.0.1   00:02:02:34:72:a51
------- vendorDetails -------
isPrivate => False
companyAddress => Times House UK CB4 5LH GB
oui => 000202
countryCode => GB
companyName => Amino Communications, Ltd
------- macAddressDetails -------
administrationType => UAA
comment => 
virtualMachine => Not detected
isValid => False
applications => []
wiresharkNotes => No details
searchTerm => 00:02:02:34:72:a51
transmissionType => unicast
------- blockDetails -------
blockFound => True
blockSize => 16777216
dateCreated => 2000-11-09
borderLeft => 000202000000
assignmentBlockSize => MA-L
borderRight => 000202FFFFFF
dateUpdated => 2015-09-27

=======
	#docker run --env API_KEY="Your api key" get_macaddr:0.0.1 [MAC Address]
>>>>>>> 35da9aa09f4152c9eaa58ca9e428b04e8ede643e
