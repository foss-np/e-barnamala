eBarnamala is a visual learning tool targeted for early learners. Its one of the few available software tools in Nepali language. It is the original work by Pravin Joshi.

Few things were off the bit. The byte codes were not portable so the added compile.py is responsible for compiling into .pyc

Python wx bindings and PIL modules are required for this tool. So make sure you have those in your system to use the tool.

Also, this tool requires changing the working directory to the eBarnamala, otherwise it will throw errors (This needs to be fixed and will be updated ASAP).

You'll need to copy the two fonts in the ./eBarnamala/fonts/ directory to global /usr/share/fonts/truetype or to $HOME/.fonts directory.
