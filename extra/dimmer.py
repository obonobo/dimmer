#!/usr/bin/env python3

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(background='black')
    root.wm_attributes('-alpha', '0.7')
    root.attributes('-type', 'dock')
    root.attributes('-alpha', 0.7)
    root.attributes('-topmost', True)
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    root.lift()
    root.mainloop()


if __name__ == '__main__':
    main()
