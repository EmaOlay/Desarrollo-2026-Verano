"""
Módulo principal de automatización que combina detección y clic.
"""
import time
from pathlib import Path
from typing import Optional, Callable
from dataclasses import dataclass, field

from core.detector import ImageDetector, DetectionResult
from core.clicker import MouseController, ClickType
from config.settings import BEHAVIOR_CONFIG
from utils.logger import get_logger


@dataclass
class AutomationResult:
    """Resultado de una operación de automatización."""
    success: bool
    detection: Optional[DetectionResult] = None
    clicked_at: Optional[tuple] = None
    attempts: int = 0
    message: str = ""


class ImageClickAutomation:
    """Clase principal para automatizar detección y clic de imágenes."""
    
    def __init__(
        self,
        detector: ImageDetector = None,
        clicker: MouseController = None,
        scan_interval: float = None,
        max_retries: int = None
    ):
        """
        Inicializa la automatización.
        
        Args:
            detector: Instancia de ImageDetector
            clicker: Instancia de MouseController
            scan_interval: Intervalo entre escaneos
            max_retries: Máximo número de intentos
        """
        self.detector = detector or ImageDetector()
        self.clicker = clicker or MouseController()
        self.scan_interval = scan_interval or BEHAVIOR_CONFIG["scan_interval"]
        self.max_retries = max_retries or BEHAVIOR_CONFIG["max_retries"]
        self.logger = get_logger(__name__)
        
        self._running = False
    
    def find_and_click(
        self,
        image_path: Path,
        click_type: ClickType = ClickType.LEFT,
        wait_for_image: bool = True,
        on_found: Optional[Callable[[DetectionResult], None]] = None
    ) -> AutomationResult:
        """
        Busca una imagen y hace clic en ella.
        
        Args:
            image_path: Ruta a la imagen a buscar
            click_type: Tipo de clic a realizar
            wait_for_image: Si debe esperar a que aparezca la imagen
            on_found: Callback cuando se encuentra la imagen
            
        Returns:
            AutomationResult con el resultado de la operación
        """
        self.logger.info(f"Buscando imagen: {image_path.name}")
        attempts = 0
        
        while attempts < self.max_retries:
            attempts += 1
            
            # Detectar imagen
            detection = self.detector.detect(image_path)
            
            if detection.found:
                self.logger.info(f"Imagen encontrada en intento {attempts}")
                
                # Callback opcional
                if on_found:
                    on_found(detection)
                
                # Obtener centro y hacer clic
                center = detection.center
                if center:
                    click_success = self.clicker.click(
                        center[0], center[1],
                        click_type=click_type
                    )
                    
                    if click_success:
                        self.logger.info(f"Clic exitoso en ({center[0]}, {center[1]})")
                        return AutomationResult(
                            success=True,
                            detection=detection,
                            clicked_at=center,
                            attempts=attempts,
                            message="Imagen encontrada y clic realizado"
                        )
            
            if not wait_for_image:
                break
                
            self.logger.debug(f"Intento {attempts}/{self.max_retries} - Imagen no encontrada")
            time.sleep(self.scan_interval)
        
        self.logger.warning(f"Imagen no encontrada después de {attempts} intentos")
        return AutomationResult(
            success=False,
            attempts=attempts,
            message=f"Imagen no encontrada después de {attempts} intentos"
        )
    
    def find_and_click_continuous(
        self,
        image_path: Path,
        click_type: ClickType = ClickType.LEFT,
        stop_after_clicks: int = None
    ) -> int:
        """
        Busca y hace clic en la imagen continuamente.
        
        Args:
            image_path: Ruta a la imagen
            click_type: Tipo de clic
            stop_after_clicks: Detener después de N clics (None = infinito)
            
        Returns:
            Número total de clics realizados
        """
        self._running = True
        clicks_count = 0
        
        self.logger.info("Iniciando modo continuo")
        
        try:
            while self._running:
                result = self.find_and_click(
                    image_path,
                    click_type=click_type,
                    wait_for_image=False
                )
                
                if result.success:
                    clicks_count += 1
                    self.logger.info(f"Clics totales: {clicks_count}")
                    
                    if stop_after_clicks and clicks_count >= stop_after_clicks:
                        self.logger.info("Límite de clics alcanzado")
                        break
                
                time.sleep(self.scan_interval)
                
        except KeyboardInterrupt:
            self.logger.info("Detenido por el usuario")
        
        self._running = False
        return clicks_count
    
    def stop(self):
        """Detiene la ejecución continua."""
        self._running = False
        self.logger.info("Solicitud de detención recibida")
