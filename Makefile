deploy: venv update.py
	git submodule update --recursive --remote
	venv/bin/python update.py
venv: requirements.txt
	test -d venv || virtualenv -p python3 venv
	venv/bin/pip install -Ur requirements.txt
clean:
	@test -d venv && rm -rf venv || echo "no venv"
	@test -d dist && rm -rf dist || echo "no dist"
	@test -d build && rm -rf build || echo "no build"
	@test -d shikari.egg-info && rm -rf shikari.egg-info || echo "no egg"
