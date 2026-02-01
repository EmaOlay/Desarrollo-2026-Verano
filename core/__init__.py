"""
Módulos core de la aplicación.
"""
from core.detector import ImageDetector, DetectionResult
from core.clicker import MouseController, ClickType
from core.automation import ImageClickAutomation, AutomationResult
from core.window import get_window_region, focus_window, WindowRegion

__all__ = [
    "ImageDetector",
    "DetectionResult",
    "MouseController", 
    "ClickType",
    "ImageClickAutomation",
    "AutomationResult",
    "get_window_region",
    "focus_window",
    "WindowRegion"
]
