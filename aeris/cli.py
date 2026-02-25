import sys
from aeris.ui.factory import AerisFactory

def main():
    app = AerisFactory()
    app.run()

if __name__ == "__main__":
    main()
