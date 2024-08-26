from distutils.core import setup, Extension

def main():
    setup(name="cik_core",
          version="1.0.0",
          description="C++ pynamics",
          author="<Abra6325,Relizc>",
          author_email="abra6325@outlook.com",
          ext_modules=[Extension("cik_core", ["cik_core.cpp", "cik_interface.cpp"])])

if __name__ == "__main__":
    main()