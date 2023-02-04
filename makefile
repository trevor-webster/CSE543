
build: reflector.py
	python3.7 -m pip install scapy==2.4.5
	cp reflector.py reflector
	chmod +x reflector
	
clean:
	rm -rf __pycache__