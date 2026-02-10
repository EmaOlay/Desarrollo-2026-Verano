"""
Módulo para manejo de ventanas de Windows.
"""
import pygetwindow as gw
from typing import Optional, Tuple
from dataclasses import dataclass


@dataclass
class WindowRegion:
    """Región de una ventana en pantalla."""
    x: int
    y: int
    width: int
    height: int
    
    def as_tuple(self) -> Tuple[int, int, int, int]:
        """Retorna la región como tupla (x, y, width, height)."""
        return (self.x, self.y, self.width, self.height)


def find_window(title: str, partial_match: bool = True) -> Optional[gw.Window]:
    """
    Busca una ventana por su título.
    
    Args:
        title: Título de la ventana a buscar
        partial_match: Si buscar coincidencia parcial
        
    Returns:
        La ventana encontrada o None
    """
    try:
        if partial_match:
            windows = gw.getWindowsWithTitle(title)
            return windows[0] if windows else None
        else:
            return gw.getWindowsWithTitle(title)[0]
    except (IndexError, Exception):
        return None


def get_window_region(title: str) -> Optional[WindowRegion]:
    """
    Obtiene la región de una ventana por su título.
    
    Args:
        title: Título de la ventana
        
    Returns:
        WindowRegion con las coordenadas o None si no se encuentra
    """
    window = find_window(title)
    
    if window is None:
        return None
    
    # Asegurarse de que la ventana esté visible
    if window.isMinimized:
        window.restore()
    
    return WindowRegion(
        x=window.left,
        y=window.top,
        width=window.width,
        height=window.height
    )


def focus_window(title: str) -> bool:
    """
    Trae una ventana al frente.
    
    Args:
        title: Título de la ventana
        
    Returns:
        True si se pudo enfocar la ventana
    """
    window = find_window(title)
    
    if window is None:
        return False
    
    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
    except Exception:
        return False
