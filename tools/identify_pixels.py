#!/usr/bin/env python3
"""
Herramienta para identificar píxeles específicos a monitorear.
Mueve el mouse sobre el área donde aparece el dado y presiona ESPACIO.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.pixel_detector import PixelDetector
from core.window import get_window_region, focus_window
import pyautogui
import keyboard


WINDOW_TITLE = "CorruptionTown"


def main():
    print("=" * 60)
    print("Herramienta de Identificación de Píxeles")
    print("=" * 60)
    print()
    print("Buscando ventana del juego...")
    
    region = get_window_region(WINDOW_TITLE)
    if region is None:
        print(f"Error: No se encontró '{WINDOW_TITLE}'")
        return 1
    
    focus_window(WINDOW_TITLE)
    time.sleep(0.2)
    
    print(f"Ventana encontrada: {region.width}x{region.height}")
    print()
    print("INSTRUCCIONES:")
    print("1. Mueve el mouse sobre el área donde aparece el dado (6)")
    print("2. Presiona ESPACIO para capturar píxeles")
    print("3. Repite varias veces en diferentes puntos del dado")
    print("4. Presiona 'Q' para terminar y generar el código")
    print()
    print("Presiona ESPACIO para empezar...")
    
    keyboard.wait('space')
    print("\n¡Listo! Ahora mueve el mouse y presiona ESPACIO en cada punto")
    print("(Presiona Q para terminar)\n")
    
    pixels = []
    
    while True:
        if keyboard.is_pressed('q'):
            break
            
        if keyboard.is_pressed('space'):
            x, y, color = PixelDetector.get_mouse_position_and_color()
            pixels.append((x, y, color))
            print(f"✓ Píxel {len(pixels)}: pos=({x}, {y}), color=RGB{color}")
            time.sleep(0.3)  # Evitar múltiples capturas
    
    if not pixels:
        print("\nNo se capturaron píxeles")
        return 1
    
    print("\n" + "=" * 60)
    print(f"Se capturaron {len(pixels)} píxeles")
    print("=" * 60)
    print("\nCódigo generado para main.py:\n")
    print("# Píxeles a monitorear (copiar esto al main.py)")
    print("PIXEL_CONDITIONS = [")
    for x, y, color in pixels:
        print(f"    PixelCondition(x={x}, y={y}, expected_color={color}, tolerance=15),")
    print("]")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
