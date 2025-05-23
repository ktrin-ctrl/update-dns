This is a simple containerized python script to update a DNS record on the  
NearlyFreeSpeech.NET DNS server based on the dynamic IP of the machine the container 
runs on. 

It uses the NFSN API, which is long in the tooth. If you'd like to adapt it for your
uses, add a file secret_credentials.py with two variables, username and api_key. 

Of course you will also want to update the subdomain and domain names in the actual script as well. 

(C)opyright 2025 Kristina Trinity, released under GPL v3.