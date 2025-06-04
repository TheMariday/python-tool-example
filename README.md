[![Supported Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)]()

[![Test Workflow](https://github.com/TheMariday/python-tool-example/actions/workflows/test_workflow.yml/badge.svg)](https://github.com/TheMariday/python-tool-example/actions/workflows/test_workflow.yml)

### Example Python Project!

Write your readme here!

## Step 0: Install

If you're on Windows, first install UV with

`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` 

Or if you're using Linux or Mac

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Once UV is installed, install marimapper with

`uv tool install marimapper --from git+https://github.com/TheMariday/marimapper`

You can run the scripts anywhere by just typing them into a console.

If you're working on the tool and developing it, create a venv and use `pip install -e .` instead

## Step 1: Test your installation

Type `my_example --help` to list the help for your tool

## Step 2: Run test:

install `pytest` with `pip install pytest`

Type `pytest .` in the root project directory to run the tests

## Step 3: Do stuff!

Do stuff here!