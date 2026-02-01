"""
Módulo de control del mouse y clics.
"""
import pyautogui
import time
from typing import Optional, Tuple
from enum import Enum

from config.settings import BEHAVIOR_CONFIG


class ClickType(Enum):
    """Tipos de clic disponibles."""
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"
    DOUBLE = "double"


class MouseController:
    """Controlador del mouse para realizar clics."""
    
    def __init__(
        self,
        click_delay: float = None,
        click_duration: float = None
    ):
        """
        Inicializa el controlador del mouse.
        
        Args:
            click_delay: Delay antes de hacer clic
            click_duration: Duración del clic
        """
        self.click_delay = click_delay or BEHAVIOR_CONFIG["click_delay"]
        self.click_duration = click_duration or BEHAVIOR_CONFIG["click_duration"]
        
        # Configuración de seguridad de pyautogui
        pyautogui.FAILSAFE = True  # Mover mouse a esquina superior izquierda para abortar
        pyautogui.PAUSE = 0.0      # Sin pausa - máxima velocidad
    
    def click(
        self,
        x: int,
        y: int,
        click_type: ClickType = ClickType.LEFT,
        clicks: int = 1
    ) -> bool:
        """
        Realiza un clic en las coordenadas especificadas.
        
        Args:
            x: Coordenada X
            y: Coordenada Y
            click_type: Tipo de clic
            clicks: Número de clics
            
        Returns:
            True si el clic fue exitoso
        """
        try:
            time.sleep(self.click_delay)
            
            if click_type == ClickType.DOUBLE:
                pyautogui.doubleClick(x, y, duration=self.click_duration)
            else:
                pyautogui.click(
                    x, y,
                    button=click_type.value,
                    clicks=clicks,
                    duration=self.click_duration
                )
            
            return True
            
        except Exception as e:
            print(f"Error al hacer clic: {e}")
            return False
    
    def move_to(self, x: int, y: int, duration: float = 0.2) -> bool:
        """
        Mueve el mouse a las coordenadas especificadas.
        
        Args:
            x: Coordenada X
            y: Coordenada Y
            duration: Duración del movimiento
            
        Returns:
            True si el movimiento fue exitoso
        """
        try:
            pyautogui.moveTo(x, y, duration=duration)
            return True
        except Exception as e:
            print(f"Error al mover mouse: {e}")
            return False
    
    @staticmethod
    def get_position() -> Tuple[int, int]:
        """Retorna la posición actual del mouse."""
        return pyautogui.position()
    
    @staticmethod
    def get_screen_size() -> Tuple[int, int]:
        """Retorna el tamaño de la pantalla."""
        return pyautogui.size()
