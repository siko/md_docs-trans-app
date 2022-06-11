from md_translate.file_translator import FileTranslator
from md_translate.files_worker import TraversalFun
from md_translate.logs import logger
from md_translate.settings import Settings


class App:
    def __init__(self) -> None:
        self.settings = Settings()

    def process(self) -> None:
        logger.info(self.settings.path)
        logger.info(self.settings.dist_path)

        _original_dir = self.settings.path
        _dist_dir = self.settings.dist_path

        files_to_process = TraversalFun(_original_dir, _dist_dir)
        files_to_process.traversal_dir()

        logger.info(f'Processing: {", ".join([f.name for f in files_to_process.md_files_list])}')

        for file_path in files_to_process.md_files_list:
            with FileTranslator(self.settings, file_path) as processing_file:
                processing_file.translate()
            logger.success('Processed: {file_path}'.format(file_path=file_path))



def run() -> None:
    try:
        App().process()
        exit(0)
    except Exception as err:
        logger.exception(err)
        exit(1)


if __name__ == "__main__":
    run()
