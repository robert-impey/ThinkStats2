#!/usr/bin/env python3

"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# (ThinkStats2) robert@iset ThinkStats2/code (master) » python
# Python 3.12.12 | packaged by conda-forge | (main, Oct 22 2025, 23:34:53) [Clang 19.1.7 ] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import nsfg
# >>> import chap01ex
# >>> import importlib
# >>>
# >>>
# >>> resp = nsfg.ReadFemResp()
# >>>
# >>>
# >>> resp
# ... Edit ...
# >>> importlib.reload(chap01ex)
# <module 'chap01ex' from '/Users/robert/code/ThinkStats2/code/chap01ex.py'>
# >>>
# >>> chap01ex.main(resp)


from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def main(resp):
    """Tests the functions in this module.

    script: string script name
    """

    print(resp.pregnum.value_counts().sort_index())


if __name__ == '__main__':
    resp = nsfg.ReadFemResp()
    main(resp)
