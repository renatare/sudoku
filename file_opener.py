from loginimas import logger

class FileOpener():
    def read_from_file(self, filename):
        gameboard = []
        try:
            with open(filename, 'r') as file:
                for line in file.readlines():
                    gameboard_line = [int(element) for element in line.strip()]
                    gameboard.append(gameboard_line)
            return gameboard
        except Exception as exception:
            logger.error(f"\n Klaida {exception},\n")
            raise

    def upload_to_file(self, filename, content):
        with open(filename, 'w', encoding="utf-8") as failas:
            failas.write(content)
            failas.close()

    def append_to_file(self, filename, content):
        with open(filename, 'a', encoding="utf-8") as failas:
            failas.write(content)
            failas.close()
