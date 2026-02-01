"""
Utilidades de logging para el proyecto.
"""
import logging
import sys
from pathlib import Path
from typing import Optional

from config.settings import LOGGING_CONFIG, LOGS_DIR


def setup_logging(
    level: str = None,
    log_file: Optional[Path] = None
) -> None:
    """
    Configura el sistema de logging.
    
    Args:
        level: Nivel de logging (DEBUG, INFO, WARNING, ERROR)
        log_file: Archivo donde guardar los logs
    """
    level = level or LOGGING_CONFIG["level"]
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # Formato del log
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )
    
    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    
    # Configurar logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    
    # Handler para archivo si está habilitado
    if LOGGING_CONFIG["file_logging"] or log_file:
        LOGS_DIR.mkdir(exist_ok=True)
        log_file = log_file or LOGS_DIR / "automation.log"
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        root_logger.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """
    Obtiene un logger configurado.
    
    Args:
        name: Nombre del logger
        
    Returns:
        Logger configurado
    """
    return logging.getLogger(name)
