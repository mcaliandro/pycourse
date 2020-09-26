#!/usr/bin/env python3

# Welcome to this introduction to Python
# First hints about Python: 
#    - everything put after the hash character (#) is a comment
#    - the first line (#!/usr/bin/env python3) is very useful to run the Python
#      script as a Linux console script (that means you don't need to enter into
#      a Python console to run Python scripts), unfortunately this doesn't work 
#      in Windows, unless you have the Bash shell installed.

# a huge string can be specified within triple-" and triple-" characters

message = """
Welcome to this introduction to Python
First hints about Python: 
    - everything put after the hash character (#) is a comment
    - the first line (#!/usr/bin/env python3) is very useful to run the Python
      script as a Linux console script (that means you don't need to enter into
      a Python console to run Python scripts), unfortunately this doesn't work 
      in Windows, unless you have the Bash shell installed.
"""

print(message)
