# Golden Die Clicker - Guía de Uso

## 🚀 Formas de Ejecutar

### Opción 1: Doble Clic (Más Fácil)
1. Haz **doble clic** en `run.bat`
2. Posiciona el mouse a la altura del dado en 3 segundos
3. ¡Listo!

### Opción 2: PowerShell
```powershell
cd "e:\Facultad\Ing Informatica\Desarrollo_2026_Verano\image_clicker"
python main.py
```

### Opción 3: Terminal de Windows
```cmd
cd "e:\Facultad\Ing Informatica\Desarrollo_2026_Verano\image_clicker"
python main.py
```

---

## 📋 Instrucciones de Uso

1. **Abre CorruptionTown** - Asegúrate de que el juego esté corriendo

2. **Ejecuta el script** (con cualquiera de las opciones de arriba)

3. **Posiciona el mouse** 
   - Tienes **3 segundos** 
   - Coloca el cursor a la **altura** donde pasa el dado (6)
   - No importa si está en movimiento
   - Déjalo ahí hasta que terminen los 3 segundos

4. **Espera**
   - El script buscará automáticamente
   - Cuando encuentre el dado → **CLIC INSTANTÁNEO**

---

## ⚙️ Ajustes (Opcional)

Si quieres cambiar la configuración, edita `main.py`:

```python
# Líneas 26-29
CONFIDENCE = 0.7          # Precisión (0.6-0.9 recomendado)
SCAN_INTERVAL = 0.01      # Velocidad de escaneo (0.01-0.05 segundos)
STRIP_HEIGHT = 150        # Altura de búsqueda (100-250 píxeles)
```

### ¿Cuándo ajustar?

- **No detecta el dado**: Baja `CONFIDENCE` a `0.6`
- **Es muy lento**: Sube `SCAN_INTERVAL` a `0.02`
- **Quieres más precisión**: Baja `STRIP_HEIGHT` a `100`

---

## 🎯 Tips

- **Posición del mouse**: Ponlo al centro vertical del número (6)
- **Si falla**: Prueba con otra altura o baja la confianza
- **Cancelar**: Presiona `Ctrl+C` en cualquier momento
- **Abortar de emergencia**: Mueve el mouse a la esquina superior izquierda

---

## 🐛 Solución de Problemas

### "No se encontró la ventana CorruptionTown"
→ Asegúrate de que el juego esté abierto

### "Imagen no encontrada"
→ Verifica que existe `images/six.png`

### El script es lento
→ Reduce `STRIP_HEIGHT` o ajusta la altura del mouse más precisa

---

## 📁 Estructura de Archivos

```
image_clicker/
├── run.bat          ← Doble clic aquí para ejecutar
├── main.py          ← Script principal
├── README.md        ← Esta guía
├── requirements.txt ← Dependencias
├── config/          ← Configuración
├── core/            ← Módulos del programa
├── utils/           ← Utilidades
└── images/
    ├── six.png      ← Imagen del (6)
    └── golden_die.png
```
