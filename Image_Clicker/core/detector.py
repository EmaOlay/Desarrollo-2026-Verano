"""
Módulo de detección de imágenes en pantalla.
"""
import pyautogui
from pathlib import Path
from typing import Optional, Tuple
from dataclasses import dataclass

from config.settings import DETECTION_CONFIG


@dataclass
class DetectionResult:
    """Resultado de una detección de imagen."""
    found: bool
    x: Optional[int] = None
    y: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    confidence: Optional[float] = None
    
    @property
    def center(self) -> Optional[Tuple[int, int]]:
        """Retorna el centro de la imagen detectada."""
        if self.found and self.x is not None and self.y is not None:
            return (
                self.x + (self.width or 0) // 2,
                self.y + (self.height or 0) // 2
            )
        return None


class ImageDetector:
    """Clase para detectar imágenes en la pantalla."""
    
    def __init__(
        self,
        confidence: float = None,
        grayscale: bool = None,
        region: Optional[Tuple[int, int, int, int]] = None
    ):
        """
        Inicializa el detector de imágenes.
        
        Args:
            confidence: Nivel de confianza (0.0 - 1.0)
            grayscale: Si usar escala de grises
            region: Región de la pantalla a escanear (x, y, width, height)
        """
        self.confidence = confidence or DETECTION_CONFIG["confidence"]
        self.grayscale = grayscale if grayscale is not None else DETECTION_CONFIG["grayscale"]
        self.region = region or DETECTION_CONFIG["region"]
    
    def detect(self, image_path: Path) -> DetectionResult:
        """
        Detecta una imagen en la pantalla.
        
        Args:
            image_path: Ruta a la imagen a buscar
            
        Returns:
            DetectionResult con la información de la detección
        """
        if not image_path.exists():
            raise FileNotFoundError(f"Imagen no encontrada: {image_path}")
        
        try:
            location = pyautogui.locateOnScreen(
                str(image_path),
                confidence=self.confidence,
                grayscale=self.grayscale,
                region=self.region
            )
            
            if location:
                return DetectionResult(
                    found=True,
                    x=location.left,
                    y=location.top,
                    width=location.width,
                    height=location.height,
                    confidence=self.confidence
                )
            
            return DetectionResult(found=False)
            
        except pyautogui.ImageNotFoundException:
            return DetectionResult(found=False)
    
    def detect_all(self, image_path: Path) -> list[DetectionResult]:
        """
        Detecta todas las instancias de una imagen en la pantalla.
        
        Args:
            image_path: Ruta a la imagen a buscar
            
        Returns:
            Lista de DetectionResult
        """
        if not image_path.exists():
            raise FileNotFoundError(f"Imagen no encontrada: {image_path}")
        
        results = []
        try:
            locations = pyautogui.locateAllOnScreen(
                str(image_path),
                confidence=self.confidence,
                grayscale=self.grayscale,
                region=self.region
            )
            
            for location in locations:
                results.append(DetectionResult(
                    found=True,
                    x=location.left,
                    y=location.top,
                    width=location.width,
                    height=location.height,
                    confidence=self.confidence
                ))
                
        except pyautogui.ImageNotFoundException:
            pass
            
        return results
