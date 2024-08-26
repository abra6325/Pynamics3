from distutils.core import setup, Extension

def main():
    setup(name="cikmods",
          version="1.0.0",
          description="C++ pynamics",
          author="<Abra6325,Relizc>",
          author_email="abra6325@outlook.com",
          ext_modules=[Extension("cikmods", ["cikmods.cpp"])])

if __name__ == "__main__":
    main()