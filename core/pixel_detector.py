"""
Módulo de detección ultrarrápida por píxeles.
Monitorea píxeles específicos para detectar cambios.
"""
import pyautogui
from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class PixelCondition:
    """Condición de color para un píxel."""
    x: int
    y: int
    expected_color: Tuple[int, int, int]  # RGB
    tolerance: int = 10  # Tolerancia en cada canal RGB
    
    def matches(self, actual_color: Tuple[int, int, int]) -> bool:
        """Verifica si el color actual coincide con el esperado."""
        return all(
            abs(actual_color[i] - self.expected_color[i]) <= self.tolerance
            for i in range(3)
        )


class PixelDetector:
    """Detector ultrarrápido basado en píxeles."""
    
    def __init__(self, conditions: List[PixelCondition]):
        """
        Inicializa el detector de píxeles.
        
        Args:
            conditions: Lista de condiciones de píxeles a verificar
        """
        self.conditions = conditions
        pyautogui.FAILSAFE = True
    
    def check(self, require_all: bool = True) -> Optional[Tuple[int, int]]:
        """
        Verifica si los píxeles cumplen las condiciones.
        
        Args:
            require_all: Si True, todos los píxeles deben coincidir.
                        Si False, basta con que uno coincida.
        
        Returns:
            Coordenadas del primer píxel que coincide, o None
        """
        matches = []
        
        for condition in self.conditions:
            # Obtener color del píxel
            pixel_color = pyautogui.pixel(condition.x, condition.y)
            
            # Verificar si coincide
            if condition.matches(pixel_color):
                matches.append(condition)
                if not require_all:
                    # Retornar en cuanto encontremos uno
                    return (condition.x, condition.y)
        
        # Si require_all, verificar que todos coincidan
        if require_all and len(matches) == len(self.conditions):
            return (self.conditions[0].x, self.conditions[0].y)
        
        return None
    
    @staticmethod
    def get_pixel_color(x: int, y: int) -> Tuple[int, int, int]:
        """Obtiene el color de un píxel en coordenadas específicas."""
        return pyautogui.pixel(x, y)
    
    @staticmethod
    def get_mouse_position_and_color() -> Tuple[int, int, Tuple[int, int, int]]:
        """Obtiene la posición del mouse y el color del píxel bajo él."""
        pos = pyautogui.position()
        color = pyautogui.pixel(pos.x, pos.y)
        return (pos.x, pos.y, color)
