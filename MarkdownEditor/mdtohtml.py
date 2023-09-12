import tkinter as tk
from tkinter import filedialog, scrolledtext
import markdown


def render_md_to_html(md_text):
    html = markdown.markdown(md_text)
    # You can further process or style the HTML if needed
    return html


def update_preview(event=None):
    md_content = md_input.get("1.0", tk.END)
    html_content = render_md_to_html(md_content)
    html_preview.delete("1.0", tk.END)
    html_preview.insert("1.0", html_content)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            md_input.delete("1.0", tk.END)
            md_input.insert("1.0", content)


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = md_input.get("1.0", tk.END)
            file.write(content)


def main():
    global md_input, html_preview

    root = tk.Tk()
    root.title("MarkdownEditor")
    root.geometry("800x600")

    # Markdown Input
    md_input = scrolledtext.ScrolledText(root, undo=True, wrap='word')
    md_input.pack(pady=20, padx=20, side=tk.LEFT, fill=tk.BOTH, expand=True)

    # HTML Preview
    html_preview = scrolledtext.ScrolledText(root, wrap='word', bg='#f5f5f5')
    html_preview.pack(pady=20, padx=20, side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Render Button
    btn_render = tk.Button(root, text="Render", command=update_preview)
    btn_render.pack()

    # Update the preview on key release
    md_input.bind("<KeyRelease>", update_preview)

    # Menu
    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Exit", command=root.quit)

    root.mainloop()


if __name__ == "__main__":
    main()
