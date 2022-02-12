from scraper import WordlePage

page = WordlePage("https://www.nytimes.com/games/wordle/index.html")

page.setBoard()

print(page.board)