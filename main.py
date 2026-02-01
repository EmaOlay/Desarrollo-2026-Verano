#!/usr/bin/env python3
"""
Script ultra-rápido para detectar el Golden Die (6).
Busca en un cuadrado centrado en la posición del mouse.

Uso:
    1. Abre el juego y espera a que aparezca el dado
    2. Posiciona el mouse SOBRE (o cerca de) donde aparece el dado
    3. Ejecuta: python main.py
    4. El script buscará en un cuadrado de 300x300px centrado en el mouse
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.detector import ImageDetector
from core.clicker import MouseController
from core.window import get_window_region, focus_window
from config import IMAGES_DIR
from utils import setup_logging, get_logger
import pyautogui


# Configuración
WINDOW_TITLE = "CorruptionTown"
IMAGE_NAME = "six.png"
CONFIDENCE = 0.7
SCAN_INTERVAL = 0.01  # 10ms - ultra rápido
SEARCH_SIZE = 300  # Tamaño del cuadrado de búsqueda (300x300 píxeles)


def main():
    """Función principal."""
    setup_logging(level="INFO")
    logger = get_logger("main")
    
    image_path = IMAGES_DIR / IMAGE_NAME
    if not image_path.exists():
        logger.error(f"Imagen no encontrada: {image_path}")
        sys.exit(1)
    
    logger.info("=" * 60)
    logger.info("Golden Die Clicker - MODO ULTRA RÁPIDO")
    logger.info("=" * 60)
    
    # Obtener ventana
    region = get_window_region(WINDOW_TITLE)
    if region is None:
        logger.error(f"No se encontró '{WINDOW_TITLE}'")
        sys.exit(1)
    
    focus_window(WINDOW_TITLE)
    logger.info(f"Ventana: {region.width}x{region.height}")
    
    # PASO 1: Obtener posición del mouse
    logger.info("")
    logger.info("POSICIONA el mouse SOBRE el dado (o donde aparece)")
    logger.info("Tienes 3 segundos...")
    
    for i in range(3, 0, -1):
        logger.info(f"  {i}...")
        time.sleep(1)
    
    # Capturar posición del mouse
    mouse_pos = pyautogui.position()
    
    # Calcular región de búsqueda (cuadrado centrado en el mouse)
    half_size = SEARCH_SIZE // 2
    search_region = (
        max(region.x, mouse_pos.x - half_size),  # x: centrado en mouse
        max(region.y, mouse_pos.y - half_size),  # y: centrado en mouse
        SEARCH_SIZE,  # ancho: cuadrado
        SEARCH_SIZE   # height: cuadrado
    )
    
    logger.info("")
    logger.info(f"[OK] Posicion capturada: X={mouse_pos.x}, Y={mouse_pos.y}")
    logger.info(f"[OK] Buscando en cuadrado: {SEARCH_SIZE}x{SEARCH_SIZE}px")
    logger.info(f"[OK] Area reducida: {SEARCH_SIZE * SEARCH_SIZE:,} pixeles vs {region.width * region.height:,}")
    logger.info("")
    logger.info("Iniciando búsqueda ultrarrápida... (Ctrl+C para cancelar)")
    
    # Crear detector con región reducida
    detector = ImageDetector(
        confidence=CONFIDENCE,
        region=search_region
    )
    clicker = MouseController()
    
    attempts = 0
    start_time = time.time()
    
    try:
        while attempts < 1000:
            attempts += 1
            
            result = detector.detect(image_path)
            
            if result.found:
                elapsed = (time.time() - start_time) * 1000  # ms
                center = result.center
                
                logger.info("")
                logger.info(f"*** ENCONTRADO! En {elapsed:.1f}ms (intento {attempts})")
                logger.info(f"    Posicion: ({center[0]}, {center[1]})")
                
                # CLIC INMEDIATO
                clicker.click(center[0], center[1])
                logger.info("    [OK] CLIC REALIZADO")
                
                return 0
            
            time.sleep(SCAN_INTERVAL)
        
        logger.warning(f"No encontrado después de {attempts} intentos")
        return 1
        
    except KeyboardInterrupt:
        logger.info("\nCancelado")
        return 1


if __name__ == "__main__":
    sys.exit(main())
