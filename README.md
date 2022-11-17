# Resolución de Sudoku

![GitHub](https://img.shields.io/github/license/sanmacorz/resolucion-sudoku)
![GitHub](https://img.shields.io/github/commit-activity/m/sanmacorz/resolucion-sudoku)

Este proyecto es una aplicación capaz de resolver cualquier [sudoku](https://es.wikipedia.org/wiki/Sudoku) que se le configure, para esto utiliza el algoritmo de [vuelta atrás](https://es.wikipedia.org/wiki/Vuelta_atr%C3%A1s), el cuál es una [búsqueda en profundidad](https://es.wikipedia.org/wiki/B%C3%BAsqueda_en_profundidad), la cuál támbien podría ser considerada como un algoritmo de [fuerza bruta](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_fuerza_bruta).  
Todo el programa está desarrollado en el lenguaje de programación [Python](https://es.wikipedia.org/wiki/Python) e implementa su interfaz gráfica usando la librería nativa [Tkinter](https://es.wikipedia.org/wiki/Tkinter).

### Configuración del proyecto

```bash
git clone https://github.com/sanmacorz/resolucion-sudoku.git
cd resolucion-sudoku/
```

### Uso del proyecto

```bash
cd src/
python3 main.py
```

## Capturas de pantalla

La interfaz gráfica del proyecto mostrando el resultado de un sudoku:
![Screenshot1](https://user-images.githubusercontent.com/27830167/202340360-0bca045d-a3a0-41e5-b07a-6d8606df088f.png)  

La aplicación [Ksudoku](https://github.com/KDE/ksudoku) mostrando el mismo resultado, nótese que el algoritmo utilizado aquí es el de [Dancing Links](https://en.wikipedia.org/wiki/Dancing_Links):

![Screenshot2](https://user-images.githubusercontent.com/27830167/202340371-2e2921a4-b613-48bc-b8ef-f31c1d89490d.png)
