
run:
	PATH=$PATH:./drivers/ .venv/bin/python -m unittest scenarios/*

install:
	sudo apt install python3-venv python3-pip
	[ -d "./.venv" ] || python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
	wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz && mv geckodriver-v0.32.0-linux64.tar.gz drivers/ && cd drivers/ && tar -xzf geckodriver-v0.32.0-linux64.tar.gz
