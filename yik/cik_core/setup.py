from distutils.core import setup, Extension

import sys
import uuid

def main(args):
    if "-force" in args:
        print("[FORCED BUILD] adding random comment to cik_core.cpp")
        j = open("cik_core.cpp", "r")
        n = j.read()
        n += "\n//" + str(uuid.uuid4())
        x = open("cik_core.cpp", "w")
        x.write(n)
        x.close()
    setup(name="cik_core",
          version="1.0.0",
          description="C++ pynamics",
          author="<Abra6325,Relizc>",
          author_email="abra6325@outlook.com",
          ext_modules=[Extension("cik_core", ["cik_core.cpp"])])
if __name__ == "__main__":
    main(sys.argv)