from distutils.core import setup, Extension

def main():
    setup(name="fputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="<Niggerass>",
          author_email="abra6325@gmail.com",
          ext_modules=[Extension("fputs", ["fputsmodule.cpp"])])

if __name__ == "__main__":
    main()