import tkinter as tk
from tkinter import font
import os
import random
import datetime
import threading

# ─── Config ────────────────────────────────────────────
MEDITATION_SECONDS = 3 * 60  # 3 minutes

BASE_DIR       = os.path.dirname(os.path.abspath(__file__))
QUOTES_FILE    = os.path.join(BASE_DIR, "quotes.txt")
REMINDERS_FILE = os.path.join(BASE_DIR, "reminders.txt")
BELL_FILE      = os.path.join(BASE_DIR, "bell.mp3")

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def ordinal(n):
    n = int(n)
    suffix = "th" if 11 <= n % 100 <= 13 else {1:"st",2:"nd",3:"rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

DAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

def parse_date(dd_mm):
    """Parse dd/mm string → datetime.date for current or next year (whichever is future/today)."""
    parts = dd_mm.strip().replace("-", "/").split("/")
    day, month = int(parts[0]), int(parts[1])
    today = datetime.date.today()
    year = today.year
    d = datetime.date(year, month, day)
    if d < today:
        d = datetime.date(year + 1, month, day)
    return d

def date_label(dd_mm):
    """'1/4'  →  'Wed, 1 Apr'"""
    try:
        d = parse_date(dd_mm)
        return f"{DAYS[d.weekday()]}, {d.day} {MONTHS[d.month - 1][:3]}"
    except Exception:
        return dd_mm

def purge_expired_reminders():
    """Delete TEST reminders whose date was strictly before today. Rewrites the file."""
    if not os.path.exists(REMINDERS_FILE):
        return
    today = datetime.date.today()
    kept = []
    with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip()
            if not raw:
                continue
            if raw.startswith("TEST|"):
                parts = raw.split("|", 2)
                if len(parts) == 3:
                    try:
                        parts2 = parts[1].replace("-", "/").split("/")
                        day, month = int(parts2[0]), int(parts2[1])
                        year = today.year
                        d = datetime.date(year, month, day)
                        # If already passed this year, check next year too
                        if d < today:
                            d = datetime.date(year + 1, month, day)
                        # Only keep if the resolved date is today or future
                        if d >= today:
                            kept.append(raw)
                        # else: expired — drop it silently
                    except Exception:
                        kept.append(raw)  # malformed → keep to avoid data loss
                else:
                    kept.append(raw)
            else:
                kept.append(raw)  # CUSTOM lines never expire automatically
    with open(REMINDERS_FILE, "w", encoding="utf-8") as f:
        for line in kept:
            f.write(line + "\n")

def load_random_quote():
    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
        return random.choice(lines) if lines else "🔥 You showed up. That's everything."
    except FileNotFoundError:
        return "🔥 You showed up. That's everything."

def load_reminders():
    """Return list of dicts: {type, pre, date, post} for test or {type, text} for custom."""
    if not os.path.exists(REMINDERS_FILE):
        return []
    entries = []
    with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("TEST|"):
                parts = line.split("|", 2)
                if len(parts) == 3:
                    dl = date_label(parts[1])
                    entries.append({
                        "type": "test",
                        "pre":  f"Crush {parts[2]} on ",
                        "date": dl,
                        "post": " ⚔"
                    })
            elif line.startswith("CUSTOM|"):
                parts = line.split("|", 1)
                if len(parts) == 2:
                    entries.append({"type": "custom", "text": parts[1]})
    return entries

def save_reminder(entry_line):
    with open(REMINDERS_FILE, "a", encoding="utf-8") as f:
        f.write(entry_line.strip() + "\n")
# ───────────────────────────────────────────────────────

BG     = "#0a0a0f"
PANEL  = "#12121a"
BORDER = "#222233"
FG_DIM = "#888899"
FG_MID = "#d0d0e8"
FG_W   = "#ffffff"


class RitualApp:
    def __init__(self):
        self.root = tk.Tk()
        self._farewell_color = "#4f46e5"
        purge_expired_reminders()          # auto-clear past TEST reminders
        self._setup_window(560, 420)
        self._build_choice_screen()
        self.root.mainloop()

    # ── Window helpers ────────────────────────────────
    def _setup_window(self, w, h):
        r = self.root
        r.title("Morning Ritual")
        r.configure(bg=BG)
        r.resizable(False, False)
        r.attributes("-topmost", True)
        self._center(w, h)

    def _center(self, w, h):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def _accent_bar(self, parent, color, width=560):
        c = tk.Canvas(parent, width=width, height=5, bg=BG, highlightthickness=0)
        c.pack(fill="x")
        c.create_rectangle(0, 0, width, 5, fill=color, outline="")

    def _divider(self, parent):
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x", pady=(8, 12))

    # ── Widget factories ──────────────────────────────
    def _lbl(self, parent, text, size=13, bold=False, color=FG_MID,
             pady=0, wraplength=480):
        w = "bold" if bold else "normal"
        f = font.Font(family="Segoe UI", size=size, weight=w)
        lbl = tk.Label(parent, text=text, bg=BG, fg=color, font=f,
                       wraplength=wraplength, justify="center")
        lbl.pack(pady=pady)
        return lbl

    def _solid_btn(self, parent, text, bg, hover, cmd, width=20, pady=6):
        f = font.Font(family="Segoe UI", size=12, weight="bold")
        b = tk.Button(parent, text=text, command=cmd,
                      bg=bg, fg=BG, activebackground=hover, activeforeground=BG,
                      relief="flat", cursor="hand2", font=f, width=width, height=2, bd=0)
        b.pack(pady=pady, ipady=4)
        b.bind("<Enter>", lambda e: b.config(bg=hover))
        b.bind("<Leave>", lambda e: b.config(bg=bg))
        return b

    def _ghost_btn(self, parent, text, cmd, width=20, pady=4):
        f = font.Font(family="Segoe UI", size=11)
        b = tk.Button(parent, text=text, command=cmd,
                      bg=PANEL, fg="#6666aa", activebackground=BORDER,
                      activeforeground=FG_MID, relief="flat", cursor="hand2",
                      font=f, width=width, height=2, bd=0)
        b.pack(pady=pady, ipady=3)
        b.bind("<Enter>", lambda e: b.config(fg=FG_MID, bg=BORDER))
        b.bind("<Leave>", lambda e: b.config(fg="#6666aa", bg=PANEL))
        return b

    def _darken(self, c):
        return {"#22c55e":"#16a34a","#a855f7":"#9333ea",
                "#4f46e5":"#4338ca","#f59e0b":"#d97706"}.get(c, c)

    # ══════════════════════════════════════════════════
    #  SCREEN 1 — Choice
    # ══════════════════════════════════════════════════
    def _build_choice_screen(self):
        self._clear()
        self._center(560, 420)
        self._accent_bar(self.root, "#4f46e5")

        fr = tk.Frame(self.root, bg=BG)
        fr.pack(expand=True, fill="both", padx=40, pady=(20, 30))

        self._lbl(fr, "⚡  BEFORE YOU BEGIN", size=11, color="#4f46e5", pady=(0, 4))
        self._lbl(fr, "Morning Ritual", size=28, bold=True, color=FG_W, pady=(0, 6))
        self._lbl(fr, "Complete one task to unlock your computer.\nSmall wins build momentum.",
                  size=12, color=FG_DIM, pady=(0, 28))

        self._solid_btn(fr, "💪  I'll do 10 Push-Ups", "#22c55e", "#16a34a", self._done_pushups)
        self._solid_btn(fr, "🧘  3-Minute Meditation",  "#4f46e5", "#4338ca", self._start_meditation)
        self._lbl(fr, "No skipping. You've got this.", size=10, color="#444455", pady=(16, 0))

    # ══════════════════════════════════════════════════
    #  SCREEN 2 — Farewell
    # ══════════════════════════════════════════════════
    def _done_pushups(self):
        self._farewell_color = "#22c55e"
        self._show_farewell("💪  Push-ups done!", "#22c55e")

    def _meditation_done(self):
        self._farewell_color = "#a855f7"
        self._show_farewell("✨  Meditation complete!", "#a855f7")

    def _show_farewell(self, title, color):
        self._farewell_color = color
        self._clear()

        reminders = load_reminders()
        h = 500 + max(0, len(reminders) - 1) * 32
        self._center(560, h)

        self._accent_bar(self.root, color)

        # Scrollable canvas in case many reminders
        outer = tk.Frame(self.root, bg=BG)
        outer.pack(expand=True, fill="both")

        fr = tk.Frame(outer, bg=BG)
        fr.pack(expand=True, fill="both", padx=44, pady=(20, 24))

        # Title
        self._lbl(fr, title, size=22, bold=True, color=color, pady=(4, 2))
        self._divider(fr)

        # Quote
        self._lbl(fr, load_random_quote(), size=13, color=FG_MID, pady=(0, 10))

        # Reminders block
        if reminders:
            self._divider(fr)
            self._lbl(fr, "📌  Reminders", size=10, color="#555577", pady=(0, 4))
            for i, r in enumerate(reminders):
                self._render_reminder(fr, r)
                if i < len(reminders) - 1:
                    tk.Frame(fr, bg=BG, height=8).pack()

        self._divider(fr)

        # ── Button row ────────────────────────────────
        btn_row = tk.Frame(fr, bg=BG)
        btn_row.pack(pady=(4, 0))

        # Let's Roll
        f_bold = font.Font(family="Segoe UI", size=12, weight="bold")
        roll = tk.Button(btn_row, text="🚀  Let's Roll",
                         command=self.root.destroy,
                         bg=color, fg=BG, activebackground=self._darken(color),
                         activeforeground=BG, relief="flat", cursor="hand2",
                         font=f_bold, width=16, height=2, bd=0)
        roll.grid(row=0, column=0, padx=(0, 10), ipady=4)
        roll.bind("<Enter>", lambda e: roll.config(bg=self._darken(color)))
        roll.bind("<Leave>", lambda e: roll.config(bg=color))

        # Add a Date
        f_reg = font.Font(family="Segoe UI", size=11)
        add = tk.Button(btn_row, text="📅  Add a Date",
                        command=self._open_add_reminder,
                        bg=PANEL, fg="#8888bb", activebackground=BORDER,
                        activeforeground=FG_MID, relief="flat", cursor="hand2",
                        font=f_reg, width=14, height=2, bd=0)
        add.grid(row=0, column=1, ipady=4)
        add.bind("<Enter>", lambda e: add.config(fg=FG_MID, bg=BORDER))
        add.bind("<Leave>", lambda e: add.config(fg="#8888bb", bg=PANEL))

    # ══════════════════════════════════════════════════
    #  ADD REMINDER — modal popup
    # ══════════════════════════════════════════════════
    def _render_reminder(self, parent, r):
        """Render a reminder line with the date highlighted in a pill."""
        row = tk.Frame(parent, bg=BG)
        row.pack(pady=(0, 2))

        f_reg  = font.Font(family="Segoe UI", size=12)
        f_bold = font.Font(family="Segoe UI", size=12, weight="bold")

        if r["type"] == "test":
            tk.Label(row, text=r["pre"], bg=BG, fg="#c0b8f0", font=f_reg).pack(side="left")
            # Highlighted date pill
            pill = tk.Frame(row, bg="#2d2060", padx=6, pady=1)
            pill.pack(side="left")
            tk.Label(pill, text=r["date"], bg="#2d2060", fg="#a78bfa",
                     font=f_bold).pack()
            tk.Label(row, text=r["post"], bg=BG, fg="#c0b8f0", font=f_reg).pack(side="left")
        else:
            tk.Label(row, text=r["text"], bg=BG, fg="#c0b8f0", font=f_reg).pack(side="left")

    def _open_add_reminder(self):
        win = tk.Toplevel(self.root)
        win.title("Add a Date")
        win.configure(bg=BG)
        win.resizable(False, False)
        win.attributes("-topmost", True)
        win.grab_set()
        self._popup_choice(win)

    def _popup_center(self, win, w, h):
        sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
        win.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _popup_choice(self, win):
        for w in win.winfo_children(): w.destroy()
        self._popup_center(win, 400, 260)

        self._accent_bar(win, "#f59e0b", 400)
        fr = tk.Frame(win, bg=BG)
        fr.pack(expand=True, fill="both", padx=28, pady=(16, 20))

        f_title = font.Font(family="Segoe UI", size=15, weight="bold")
        f_sub   = font.Font(family="Segoe UI", size=11)
        tk.Label(fr, text="Add a Reminder", bg=BG, fg=FG_W, font=f_title).pack(pady=(0, 4))
        tk.Label(fr, text="What kind?", bg=BG, fg=FG_DIM, font=f_sub).pack(pady=(0, 16))

        def choice_btn(text, cmd):
            f = font.Font(family="Segoe UI", size=11, weight="bold")
            b = tk.Button(fr, text=text, command=cmd,
                          bg="#1e1e2e", fg=FG_MID, activebackground=BORDER,
                          activeforeground=FG_W, relief="flat", cursor="hand2",
                          font=f, width=30, height=2, bd=0)
            b.pack(pady=4, ipady=2)
            b.bind("<Enter>", lambda e: b.config(bg=BORDER))
            b.bind("<Leave>", lambda e: b.config(bg="#1e1e2e"))

        choice_btn("📝  Test / Exam",      lambda: self._popup_test(win))
        choice_btn("✏️   Custom Reminder", lambda: self._popup_custom(win))

    def _popup_test(self, win):
        for w in win.winfo_children(): w.destroy()
        self._popup_center(win, 400, 310)

        self._accent_bar(win, "#f59e0b", 400)
        fr = tk.Frame(win, bg=BG)
        fr.pack(expand=True, fill="both", padx=28, pady=(16, 18))

        f_title = font.Font(family="Segoe UI", size=15, weight="bold")
        f_lbl   = font.Font(family="Segoe UI", size=10)
        f_ent   = font.Font(family="Segoe UI", size=12)
        f_b     = font.Font(family="Segoe UI", size=11, weight="bold")

        tk.Label(fr, text="📝  Add Test / Exam", bg=BG, fg=FG_W, font=f_title).pack(pady=(0, 14))

        tk.Label(fr, text="Date  (dd/mm  —  day auto-calculated)", bg=BG, fg=FG_DIM, font=f_lbl, anchor="w").pack(fill="x")
        date_var = tk.StringVar()
        date_ent = tk.Entry(fr, textvariable=date_var, font=f_ent,
                            bg="#1a1a2e", fg=FG_W, insertbackground=FG_W,
                            relief="flat", bd=0)
        date_ent.pack(fill="x", ipady=6, pady=(2, 10))
        date_ent.focus()

        tk.Label(fr, text="Topic / Subject", bg=BG, fg=FG_DIM, font=f_lbl, anchor="w").pack(fill="x")
        topic_var = tk.StringVar()
        topic_ent = tk.Entry(fr, textvariable=topic_var, font=f_ent,
                             bg="#1a1a2e", fg=FG_W, insertbackground=FG_W,
                             relief="flat", bd=0)
        topic_ent.pack(fill="x", ipady=6, pady=(2, 12))

        err_var = tk.StringVar()
        tk.Label(fr, textvariable=err_var, bg=BG, fg="#ef4444", font=f_lbl).pack()

        btn_row = tk.Frame(fr, bg=BG)
        btn_row.pack(pady=(6, 0))

        def save():
            d, t = date_var.get().strip(), topic_var.get().strip()
            if not d or not t:
                err_var.set("Please fill in both fields.")
                return
            try:
                parts = d.replace("-", "/").split("/")
                assert 1 <= int(parts[0]) <= 31 and 1 <= int(parts[1]) <= 12
            except Exception:
                err_var.set("Use dd/mm format — e.g. 14/6")
                return
            save_reminder(f"TEST|{d}|{t}")
            self._popup_saved(win)

        tk.Button(btn_row, text="Save", command=save,
                  bg="#f59e0b", fg=BG, activebackground="#d97706",
                  relief="flat", cursor="hand2", font=f_b, width=10, bd=0
                  ).grid(row=0, column=0, padx=(0, 8), ipady=5)
        tk.Button(btn_row, text="← Back", command=lambda: self._popup_choice(win),
                  bg=PANEL, fg=FG_DIM, activebackground=BORDER,
                  relief="flat", cursor="hand2", font=f_b, width=10, bd=0
                  ).grid(row=0, column=1, ipady=5)

    def _popup_custom(self, win):
        for w in win.winfo_children(): w.destroy()
        self._popup_center(win, 400, 260)

        self._accent_bar(win, "#f59e0b", 400)
        fr = tk.Frame(win, bg=BG)
        fr.pack(expand=True, fill="both", padx=28, pady=(16, 18))

        f_title = font.Font(family="Segoe UI", size=15, weight="bold")
        f_lbl   = font.Font(family="Segoe UI", size=10)
        f_ent   = font.Font(family="Segoe UI", size=12)
        f_b     = font.Font(family="Segoe UI", size=11, weight="bold")

        tk.Label(fr, text="✏️  Custom Reminder", bg=BG, fg=FG_W, font=f_title).pack(pady=(0, 14))
        tk.Label(fr, text="Your message (shown as-is)", bg=BG, fg=FG_DIM,
                 font=f_lbl, anchor="w").pack(fill="x")

        msg_var = tk.StringVar()
        msg_ent = tk.Entry(fr, textvariable=msg_var, font=f_ent,
                           bg="#1a1a2e", fg=FG_W, insertbackground=FG_W,
                           relief="flat", bd=0)
        msg_ent.pack(fill="x", ipady=6, pady=(2, 12))
        msg_ent.focus()

        err_var = tk.StringVar()
        tk.Label(fr, textvariable=err_var, bg=BG, fg="#ef4444", font=f_lbl).pack()

        btn_row = tk.Frame(fr, bg=BG)
        btn_row.pack(pady=(6, 0))

        def save():
            m = msg_var.get().strip()
            if not m:
                err_var.set("Please enter a message.")
                return
            save_reminder(f"CUSTOM|{m}")
            self._popup_saved(win)

        tk.Button(btn_row, text="Save", command=save,
                  bg="#f59e0b", fg=BG, activebackground="#d97706",
                  relief="flat", cursor="hand2", font=f_b, width=10, bd=0
                  ).grid(row=0, column=0, padx=(0, 8), ipady=5)
        tk.Button(btn_row, text="← Back", command=lambda: self._popup_choice(win),
                  bg=PANEL, fg=FG_DIM, activebackground=BORDER,
                  relief="flat", cursor="hand2", font=f_b, width=10, bd=0
                  ).grid(row=0, column=1, ipady=5)

    def _popup_saved(self, win):
        for w in win.winfo_children(): w.destroy()
        self._popup_center(win, 400, 200)

        self._accent_bar(win, "#22c55e", 400)
        fr = tk.Frame(win, bg=BG)
        fr.pack(expand=True, fill="both", padx=28, pady=20)

        f_big = font.Font(family="Segoe UI", size=18, weight="bold")
        f_sub = font.Font(family="Segoe UI", size=11)
        f_b   = font.Font(family="Segoe UI", size=11, weight="bold")

        tk.Label(fr, text="✅  Reminder Saved!", bg=BG, fg="#22c55e", font=f_big).pack(pady=(8, 4))
        tk.Label(fr, text="You'll see it every session until removed.",
                 bg=BG, fg=FG_DIM, font=f_sub).pack(pady=(0, 16))

        btn_row = tk.Frame(fr, bg=BG)
        btn_row.pack()

        tk.Button(btn_row, text="Add Another",
                  command=lambda: self._popup_choice(win),
                  bg=PANEL, fg=FG_DIM, activebackground=BORDER,
                  relief="flat", cursor="hand2", font=f_b, width=12, bd=0
                  ).grid(row=0, column=0, padx=(0, 8), ipady=5)

        def done():
            win.destroy()
            self._show_farewell(
                "💪  Push-ups done!" if self._farewell_color == "#22c55e"
                else "✨  Meditation complete!",
                self._farewell_color
            )

        tk.Button(btn_row, text="Done",
                  command=done,
                  bg="#22c55e", fg=BG, activebackground="#16a34a",
                  relief="flat", cursor="hand2", font=f_b, width=12, bd=0
                  ).grid(row=0, column=1, ipady=5)

    # ══════════════════════════════════════════════════
    #  MEDITATION TIMER
    # ══════════════════════════════════════════════════
    def _start_meditation(self):
        self._clear()
        self._center(560, 420)
        self._accent_bar(self.root, "#a855f7")

        fr = tk.Frame(self.root, bg=BG)
        fr.pack(expand=True, fill="both", padx=40, pady=(20, 30))

        self._lbl(fr, "🧘  MEDITATION",   size=11, color="#a855f7", pady=(0, 4))
        self._lbl(fr, "Find Your Center", size=24, bold=True, color=FG_W, pady=(0, 8))
        self._lbl(fr, "Close your eyes. Focus on your breath.\nLet thoughts pass like clouds.",
                  size=12, color=FG_DIM, pady=(0, 20))

        timer_font = font.Font(family="Segoe UI", size=52, weight="bold")
        self.timer_var = tk.StringVar(value=self._fmt(MEDITATION_SECONDS))
        tk.Label(fr, textvariable=self.timer_var, bg=BG, fg="#a855f7",
                 font=timer_font).pack(pady=(0, 6))

        self.status_var = tk.StringVar(value="Breathe in…")
        tk.Label(fr, textvariable=self.status_var, bg=BG, fg="#555566",
                 font=font.Font(family="Segoe UI", size=11)).pack()

        self.prog_cv = tk.Canvas(fr, width=400, height=8, bg="#1a1a2e",
                                 highlightthickness=0)
        self.prog_cv.pack(pady=(20, 0))
        self.prog_bar = self.prog_cv.create_rectangle(0, 0, 0, 8, fill="#a855f7", outline="")

        self.remaining = MEDITATION_SECONDS
        self._tick()

    def _fmt(self, secs):
        m, s = divmod(secs, 60)
        return f"{m:02d}:{s:02d}"

    def _tick(self):
        if self.remaining <= 0:
            self._meditation_done()
            return
        self.timer_var.set(self._fmt(self.remaining))
        phase = (MEDITATION_SECONDS - self.remaining) % 8
        self.status_var.set("Breathe in…" if phase < 4 else "Breathe out…")
        frac = (MEDITATION_SECONDS - self.remaining) / MEDITATION_SECONDS
        self.prog_cv.coords(self.prog_bar, 0, 0, 400 * frac, 8)
        self.remaining -= 1
        self.root.after(1000, self._tick)

    def _play_bell(self):
        """Play bell.mp3 in a background thread so UI doesn't freeze."""
        def _play():
            try:
                import winsound
                # winsound can't play mp3 natively — use playsound if available
                raise ImportError
            except ImportError:
                pass
            try:
                from playsound import playsound
                playsound(BELL_FILE)
                return
            except Exception:
                pass
            # Fallback: use Windows Media Player via subprocess (no extra install)
            try:
                import subprocess
                subprocess.Popen(
                    ["powershell", "-c",
                     f'(New-Object Media.SoundPlayer).PlaySync() ; '
                     f'Add-Type -AssemblyName presentationCore ; '
                     f'$mp = [System.Windows.Media.MediaPlayer]::new() ; '
                     f'$mp.Open([Uri]::new("{BELL_FILE}")) ; '
                     f'Start-Sleep -m 500 ; $mp.Play() ; Start-Sleep 5'],
                    creationflags=0x08000000  # no window
                )
            except Exception:
                pass
        threading.Thread(target=_play, daemon=True).start()

    def _meditation_done(self):
        self._play_bell()
        self._farewell_color = "#a855f7"
        self._show_farewell("✨  Meditation complete!", "#a855f7")

if __name__ == '__main__':
    RitualApp()
