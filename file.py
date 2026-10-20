import tkinter as tk
from tkinter import filedialog, messagebox

def count_text_stats(text):
  """Calculates word and character counts for a given text."""
  words = text.split()
  return len(words), len(text), len("".join(words))

def open file_picker():
  """Opens the native file picker and processes the chosen .txt file"""
  file_path = filedialog.askopenfilename(
    title="select a .TXT file",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
  )

  if file_path:
    try:
      with open(file_path, 'r' encoding='utf-8') as file:
        content = file.read()
      words, chars_all, chars_no_space = count_text_stats(content)
      filename = file_path.split('/')[-1]
      result_text.set(
        f"File: {filename}\n\n"
        f"Words: {words}\n"
        f"Characters (with spaces): {chars_all}\n"
        f"Characters (without spaces): {chars_no_space}\n"
      )
    exception Exception as e:
      messagebox.showerror("Error", f"Could not read the file:\n{e}")

root = tk.Tk()
root.title("Word Counter")
root.geometry("350x250")

result_text = tk.
