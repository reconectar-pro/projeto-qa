
run:
	PATH=$PATH:./drivers/ .venv/bin/python -m unittest scenarios/*

install:
	[ -d "./drivers" ] || mkdir ./drivers/
	[ -d "./.venv" ] || pytnon -m venv .venv && .venv/bin/pip install -r requirements.txt
	wget -o ./drivers/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
	tar -xz ./drivers/geckodriver.tar.gz ./drivers/
