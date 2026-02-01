"""
Configuración global del proyecto.
"""
from pathlib import Path

# Rutas del proyecto
PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"
LOGS_DIR = PROJECT_ROOT / "logs"

# Configuración de detección
DETECTION_CONFIG = {
    "confidence": 0.8,          # Nivel de confianza para detectar la imagen (0.0 - 1.0)
    "grayscale": False,         # Usar escala de grises para búsqueda más rápida
    "region": None,             # Región de pantalla a escanear (x, y, width, height) o None para toda
}

# Configuración de comportamiento - OPTIMIZADO PARA UN SOLO CLIC RÁPIDO
BEHAVIOR_CONFIG = {
    "click_delay": 0.0,         # Sin delay - clic instantáneo
    "scan_interval": 0.05,      # Escaneo muy rápido (50ms)
    "max_retries": 100,         # Muchos intentos para no perder la imagen
    "click_duration": 0.0,      # Clic instantáneo
}

# Configuración de logging
LOGGING_CONFIG = {
    "enabled": True,
    "level": "INFO",            # DEBUG, INFO, WARNING, ERROR
    "file_logging": False,
}
