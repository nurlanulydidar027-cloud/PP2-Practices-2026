"""
=====================================================================
  PAINT — Practice 11
  Расширение проекта из Practice 8. Добавлены фигуры:
    1) Квадрат
    2) Прямоугольный треугольник
    3) Равносторонний треугольник
    4) Ромб
    5) Подробные комментарии в коде
  Также: карандаш, линия, прямоугольник, эллипс, ластик,
         выбор цвета, размер кисти, заливка, отмена, очистка, сохранение.
=====================================================================
Запуск:  python paint.py
"""

import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
import math


class PaintApp:
    """Главный класс приложения Paint."""

    # ---------- Цвета и стили UI ----------
    BG_DARK     = "#15151e"
    PANEL_BG    = "#1f1f2a"
    BTN_BG      = "#3a3a4d"
    BTN_ACTIVE  = "#5050a0"
    BTN_FG      = "#ffffff"
    CANVAS_BG   = "#0e0e16"

    def __init__(self, root):
        self.root = root
        self.root.title("Paint — Practice 11")
        self.root.geometry("1180x740")
        self.root.configure(bg=self.PANEL_BG)
        self.root.minsize(900, 600)

        # ---- Состояние рисования ----
        self.current_tool   = "pencil"   # Текущий инструмент
        self.current_color  = "#ffffff"  # Текущий цвет
        self.brush_size     = 3          # Толщина кисти
        self.fill_shapes    = False      # Заливка фигур
        self.start_x        = None       # Начальная точка для фигур
        self.start_y        = None
        self.preview_id     = None       # ID превью при перетаскивании
        self.last_x         = 0          # Для непрерывного карандаша
        self.last_y         = 0

        # Стек ID нарисованных объектов для функции undo
        self.history = []

        # Сборка интерфейса
        self._build_toolbar()
        self._build_canvas()
        self._build_status_bar()
        self._bind_events()

    # =================================================================
    #  Построение интерфейса
    # =================================================================
    def _build_toolbar(self):
        """Верхняя панель инструментов."""
        toolbar = tk.Frame(self.root, bg=self.PANEL_BG)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=8, pady=8)

        # ----- Инструменты -----
        tools_frame = tk.LabelFrame(toolbar, text="Tools",
                                    fg=self.BTN_FG, bg=self.PANEL_BG,
                                    padx=6, pady=4,
                                    font=("Arial", 9, "bold"))
        tools_frame.pack(side=tk.LEFT, padx=4)

        tools = [
            ("✏ Pencil",        "pencil"),
            ("／ Line",          "line"),
            ("▭ Rect",           "rectangle"),
            ("■ Square",         "square"),
            ("◯ Ellipse",        "ellipse"),
            ("◣ R-Triangle",     "right_triangle"),
            ("△ E-Triangle",     "equilateral_triangle"),
            ("◇ Rhombus",        "rhombus"),
            ("✕ Eraser",         "eraser"),
        ]
        self.tool_buttons = {}
        for label, tool in tools:
            btn = tk.Button(tools_frame, text=label, width=12,
                            bg=self.BTN_BG, fg=self.BTN_FG,
                            relief=tk.FLAT, font=("Arial", 9),
                            activebackground=self.BTN_ACTIVE,
                            activeforeground=self.BTN_FG,
                            command=lambda t=tool: self.set_tool(t))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            self.tool_buttons[tool] = btn

        # ----- Цвет -----
        color_frame = tk.LabelFrame(toolbar, text="Color",
                                    fg=self.BTN_FG, bg=self.PANEL_BG,
                                    padx=6, pady=4,
                                    font=("Arial", 9, "bold"))
        color_frame.pack(side=tk.LEFT, padx=4)

        self.color_btn = tk.Button(color_frame, text="    ",
                                   bg=self.current_color,
                                   width=4, relief=tk.RIDGE, bd=2,
                                   command=self.choose_color)
        self.color_btn.pack(side=tk.LEFT, padx=4)

        # Быстрая палитра — клик по цвету сразу его выбирает
        palette = ["#ffffff", "#000000", "#ff5252", "#52ff52",
                   "#5252ff", "#ffff52", "#ff52ff", "#52ffff",
                   "#ff9933", "#9933ff", "#888888", "#aa6633"]
        for c in palette:
            sw = tk.Button(color_frame, bg=c, width=2,
                           relief=tk.FLAT,
                           command=lambda col=c: self.set_color(col))
            sw.pack(side=tk.LEFT, padx=1)

        # ----- Размер кисти и заливка -----
        opt_frame = tk.LabelFrame(toolbar, text="Brush",
                                  fg=self.BTN_FG, bg=self.PANEL_BG,
                                  padx=6, pady=4,
                                  font=("Arial", 9, "bold"))
        opt_frame.pack(side=tk.LEFT, padx=4)

        tk.Label(opt_frame, text="Size:", bg=self.PANEL_BG,
                 fg=self.BTN_FG).pack(side=tk.LEFT)
        self.size_scale = tk.Scale(opt_frame, from_=1, to=30,
                                   orient=tk.HORIZONTAL, length=110,
                                   bg=self.PANEL_BG, fg=self.BTN_FG,
                                   troughcolor=self.BTN_BG,
                                   highlightthickness=0,
                                   command=self.set_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT, padx=4)

        self.fill_var = tk.BooleanVar(value=False)
        tk.Checkbutton(opt_frame, text="Fill",
                       variable=self.fill_var,
                       bg=self.PANEL_BG, fg=self.BTN_FG,
                       selectcolor=self.BTN_BG,
                       activebackground=self.PANEL_BG,
                       activeforeground=self.BTN_FG,
                       command=self.toggle_fill).pack(side=tk.LEFT, padx=6)

        # ----- Действия с файлом -----
        act_frame = tk.LabelFrame(toolbar, text="File",
                                  fg=self.BTN_FG, bg=self.PANEL_BG,
                                  padx=6, pady=4,
                                  font=("Arial", 9, "bold"))
        act_frame.pack(side=tk.LEFT, padx=4)

        tk.Button(act_frame, text="Undo",
                  bg=self.BTN_BG, fg=self.BTN_FG, width=7,
                  relief=tk.FLAT,
                  command=self.undo).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(act_frame, text="Clear",
                  bg="#aa3333", fg=self.BTN_FG, width=7,
                  relief=tk.FLAT,
                  command=self.clear_canvas).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(act_frame, text="Save",
                  bg="#33aa55", fg=self.BTN_FG, width=7,
                  relief=tk.FLAT,
                  command=self.save_canvas).pack(side=tk.LEFT, padx=2, pady=2)

        self._update_tool_buttons()

    def _build_canvas(self):
        """Рабочая область — холст."""
        canvas_frame = tk.Frame(self.root, bg=self.BG_DARK)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 4))

        self.canvas = tk.Canvas(canvas_frame, bg=self.CANVAS_BG,
                                highlightthickness=2,
                                highlightbackground=self.BTN_ACTIVE,
                                cursor="crosshair")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def _build_status_bar(self):
        """Статусная строка снизу."""
        self.status = tk.Label(self.root, text="Ready", bd=1,
                               relief=tk.SUNKEN, anchor=tk.W,
                               bg=self.PANEL_BG, fg="#aaaacc",
                               font=("Arial", 9))
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def _bind_events(self):
        """Привязка событий мыши."""
        self.canvas.bind("<Button-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.on_motion)
        # Горячие клавиши
        self.root.bind("<Control-z>", lambda e: self.undo())
        self.root.bind("<Control-s>", lambda e: self.save_canvas())

    # =================================================================
    #  Сеттеры состояния
    # =================================================================
    def set_tool(self, tool):
        self.current_tool = tool
        self._update_tool_buttons()
        self.status.config(
            text=f"Tool: {tool.replace('_', ' ').title()}")

    def _update_tool_buttons(self):
        """Подсветка активной кнопки инструмента."""
        for tool, btn in self.tool_buttons.items():
            if tool == self.current_tool:
                btn.config(bg=self.BTN_ACTIVE, relief=tk.SUNKEN)
            else:
                btn.config(bg=self.BTN_BG, relief=tk.FLAT)

    def set_color(self, color):
        self.current_color = color
        self.color_btn.config(bg=color)

    def choose_color(self):
        color = colorchooser.askcolor(color=self.current_color)[1]
        if color:
            self.set_color(color)

    def set_size(self, val):
        self.brush_size = int(val)

    def toggle_fill(self):
        self.fill_shapes = self.fill_var.get()

    # =================================================================
    #  Обработчики мыши
    # =================================================================
    def on_press(self, event):
        """Начало рисования."""
        self.start_x, self.start_y = event.x, event.y
        if self.current_tool in ("pencil", "eraser"):
            self.last_x, self.last_y = event.x, event.y

    def on_drag(self, event):
        """Тянем мышь с зажатой кнопкой."""
        if self.start_x is None:
            return

        if self.current_tool == "pencil":
            # Карандаш: рисуем непрерывную линию между точками
            line_id = self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=self.current_color, width=self.brush_size,
                capstyle=tk.ROUND, smooth=True)
            self.history.append(line_id)
            self.last_x, self.last_y = event.x, event.y

        elif self.current_tool == "eraser":
            # Ластик: рисуем цветом фона широкой "кистью"
            line_id = self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=self.CANVAS_BG, width=self.brush_size * 3,
                capstyle=tk.ROUND)
            self.history.append(line_id)
            self.last_x, self.last_y = event.x, event.y

        else:
            # Для фигур показываем "превью" — пунктирный контур
            if self.preview_id is not None:
                self.canvas.delete(self.preview_id)
            self.preview_id = self._draw_shape(
                self.current_tool,
                self.start_x, self.start_y,
                event.x, event.y, preview=True)

    def on_release(self, event):
        """Отпустили кнопку — фиксируем фигуру."""
        if self.start_x is None:
            return

        if self.preview_id is not None:
            self.canvas.delete(self.preview_id)
            self.preview_id = None

        if self.current_tool not in ("pencil", "eraser"):
            shape_id = self._draw_shape(
                self.current_tool,
                self.start_x, self.start_y,
                event.x, event.y, preview=False)
            if shape_id:
                self.history.append(shape_id)

        self.start_x, self.start_y = None, None

    def on_motion(self, event):
        """Обновление статус-строки при движении мыши."""
        self.status.config(
            text=(f"Tool: {self.current_tool.replace('_', ' ').title()}  |  "
                  f"X: {event.x}, Y: {event.y}  |  "
                  f"Size: {self.brush_size}  |  "
                  f"Color: {self.current_color}  |  "
                  f"Fill: {'on' if self.fill_shapes else 'off'}"))

    # =================================================================
    #  Рисование фигур
    # =================================================================
    def _draw_shape(self, tool, x1, y1, x2, y2, preview=False):
        """
        Универсальный метод рисования фигур.
        x1,y1 — точка начала перетаскивания, x2,y2 — текущая позиция.
        preview=True — рисуется временный пунктирный контур.
        """
        outline = self.current_color
        fill    = self.current_color if self.fill_shapes else ""
        dash    = (4, 4) if preview else None

        # ----- Линия -----
        if tool == "line":
            return self.canvas.create_line(
                x1, y1, x2, y2,
                fill=outline, width=self.brush_size,
                dash=dash, capstyle=tk.ROUND)

        # ----- Прямоугольник -----
        if tool == "rectangle":
            return self.canvas.create_rectangle(
                x1, y1, x2, y2,
                outline=outline, fill=fill,
                width=self.brush_size, dash=dash)

        # ----- Квадрат -----
        # Берём максимум из dx и dy и сохраняем направление перетаскивания
        if tool == "square":
            dx, dy = x2 - x1, y2 - y1
            side = max(abs(dx), abs(dy))
            sx = 1 if dx >= 0 else -1
            sy = 1 if dy >= 0 else -1
            return self.canvas.create_rectangle(
                x1, y1, x1 + sx * side, y1 + sy * side,
                outline=outline, fill=fill,
                width=self.brush_size, dash=dash)

        # ----- Эллипс / круг -----
        if tool == "ellipse":
            return self.canvas.create_oval(
                x1, y1, x2, y2,
                outline=outline, fill=fill,
                width=self.brush_size, dash=dash)

        # ----- Прямоугольный треугольник -----
        # Прямой угол в одной из вершин bounding-box.
        # Углы: (x1,y1)  --(гипотенуза)--  (x2,y2)
        #            \__прямой угол при (x1, y2)
        if tool == "right_triangle":
            points = [x1, y1, x1, y2, x2, y2]
            return self.canvas.create_polygon(
                points, outline=outline, fill=fill if fill else "",
                width=self.brush_size, dash=dash)

        # ----- Равносторонний треугольник -----
        # Основание = ширина перетаскивания, высота = side * √3 / 2.
        # Направление "вверх" или "вниз" зависит от направления перетаскивания.
        if tool == "equilateral_triangle":
            side   = abs(x2 - x1)
            height = side * math.sqrt(3) / 2
            cx     = (x1 + x2) / 2
            if y2 >= y1:
                # Тянем вниз → треугольник остриём вверх
                base_y = max(y1, y2)
                points = [x1, base_y, x2, base_y, cx, base_y - height]
            else:
                # Тянем вверх → треугольник остриём вниз
                base_y = min(y1, y2)
                points = [x1, base_y, x2, base_y, cx, base_y + height]
            return self.canvas.create_polygon(
                points, outline=outline, fill=fill if fill else "",
                width=self.brush_size, dash=dash)

        # ----- Ромб -----
        # Вершины ромба — середины сторон bounding-box.
        if tool == "rhombus":
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            points = [cx, y1, x2, cy, cx, y2, x1, cy]
            return self.canvas.create_polygon(
                points, outline=outline, fill=fill if fill else "",
                width=self.brush_size, dash=dash)

        return None

    # =================================================================
    #  Действия с холстом
    # =================================================================
    def clear_canvas(self):
        """Полная очистка холста (с подтверждением)."""
        if messagebox.askyesno("Clear", "Очистить весь холст?"):
            self.canvas.delete("all")
            self.history.clear()

    def undo(self):
        """Отмена последнего действия (Ctrl+Z)."""
        if self.history:
            item = self.history.pop()
            self.canvas.delete(item)

    def save_canvas(self):
        """
        Сохранение холста. Базово — в PostScript (.ps), без зависимостей.
        Если установлен Pillow + Ghostscript — конвертирует в PNG.
        """
        try:
            from PIL import Image  # noqa: F401
            has_pil = True
        except ImportError:
            has_pil = False

        if has_pil:
            filetypes = [("PNG image", "*.png"), ("PostScript", "*.ps")]
            ext = ".png"
        else:
            filetypes = [("PostScript", "*.ps")]
            ext = ".ps"

        path = filedialog.asksaveasfilename(defaultextension=ext,
                                            filetypes=filetypes)
        if not path:
            return

        # Tkinter умеет сохранять только в PostScript "из коробки"
        ps_path = path if path.lower().endswith(".ps") else path + ".tmp.ps"
        self.canvas.update()
        self.canvas.postscript(file=ps_path, colormode="color")

        if has_pil and not path.lower().endswith(".ps"):
            try:
                from PIL import Image
                import os
                img = Image.open(ps_path)
                img.load()  # Требует Ghostscript
                img.save(path)
                os.remove(ps_path)
                messagebox.showinfo("Saved", f"Сохранено: {path}")
            except Exception as e:
                messagebox.showwarning(
                    "PNG conversion failed",
                    f"Сохранено как PostScript: {ps_path}\n"
                    f"Для PNG нужен Ghostscript.\nПричина: {e}")
        else:
            messagebox.showinfo("Saved", f"Сохранено: {ps_path}")


# =====================================================================
#  Запуск приложения
# =====================================================================
def main():
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()