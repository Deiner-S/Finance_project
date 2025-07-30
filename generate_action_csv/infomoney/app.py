from scraping import Scraping
class App:
    def __init__(self):
        self.screper = Scraping()

    def run(self):
        self.screper.run()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
