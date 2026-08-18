import logging
from app.core.config import settings

def configure_logging() -> None:
    '''
    Configures centralized logging for the workflow engine.

    The logging level is controlled through application settings so it can be configured without changing the logging code.
    '''

    logging.basicConfig(
        level=getattr(
            logging,
            settings.log_level.upper(),
            logging.INFO,
        ),
        format=(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
    )