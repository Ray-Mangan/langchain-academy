# venv

-   activating venv in mac os needs to be done with either `source .venv/bin/activate` or `. .venv/bin/activate`

# terminal stuff

-   export "API_KEY" doesn't persist between terminal sessions, you must use nano modify the shell config file `nano ~/.zshrc`. Add new lines with `export API_KEY=`, then save with ^O, press enter to confirm, then ^x to exit. Reload shell config file with `source ~/.zshrc`, then use `env` or `echo $API_KEY` to confirm

# conda

-   disable automation conda activation of base environment by altering conda config file.

# langsmith

env var OPENAI_API_KEY must exist. Can't be named as something else.
