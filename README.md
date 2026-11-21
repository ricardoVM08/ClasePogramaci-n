# Domingos en primer día de mes (siglo XX)

## Problema

¿Cuántos domingos cayeron en primer día de mes durante el siglo XX (del 1 de enero de 1901 al 31 de diciembre de 2000)?

*(Project Euler, problema 19)*

## Solución

```python
import calendar

contador = 0

for año in range(1901, 2001):
    for mes in range(1, 13):
        if calendar.weekday(año, mes, 1) == 6:
            contador += 1

print("Cantidad de domingos:", contador)
```

## Cómo funciona

- `range(1901, 2001)` recorre los años de 1901 a 2000 (el 2001 queda excluido).
- `calendar.weekday(año, mes, 1)` devuelve el día de la semana del día 1 de cada mes, donde `0` es lunes y `6` es domingo.
- Cada vez que el resultado es `6`, se incrementa el contador.

## Ejecución

```bash
python main.py
```

## Resultado

```
Cantidad de domingos: 171
```

Son 171 de 1,200 meses (≈ 14.25 %), muy cerca del 1/7 (≈ 14.29 %) esperado si los días de la semana se repartieran por igual.