# 🐮 Cow Debugger - AI-assisted Prototype

> ⚠️ This is a non-final, AI-assisted version of the Cow Debugger.

This project is a simple interpreter and step-by-step debugger for the [Cow programming language](https://esolangs.org/wiki/Cow), built with the help of ChatGPT as part of a learning process.

---

## 💻 Features

- ✅ Reads `.cow` files and filters valid Cow instructions
- 🧠 Handles all key Cow commands:
  - `MoO` / `MOo` – increment/decrement memory
  - `moO` / `mOo` – move pointer right/left
  - `Moo` – input/output based on memory
  - `MMM` – copy/paste to/from clipboard
  - `MOO` / `moo` – loop start/end
- 🖥️ Memory (100 cells), pointer, clipboard, and loop jump support
- 🧪 Interactive step-by-step execution with debug info
- 🖨️ Accumulates output (e.g., to print `HELLO WORLD`)

---

## 💡 Why Keep This Branch?

This is **not** a final version. It’s here as:

- 🧪 A proof-of-concept  
- 📸 A snapshot of my learning process  
- 📚 A reference for the clean version I plan to write fully by myself  

Future branches (like `main` or `rewrite/manual`) will reflect a **complete rewrite without AI help**.  
This way, I can look back and clearly see how I’ve improved — and hopefully inspire others to do the same.

---

## 🌱 To Do (in clean rewrite)

- [ ] ✍️ Rewrite all logic by hand, without AI  
- [ ] 🧪 Add unit tests for each command  
- [ ] 🖥️ Visual interface (maybe with `Tkinter`)  
- [ ] ⏪ Add reverse execution (step back)

---

## 📂 Example Output

You can run the script and step through Cow instructions. At the end, the output buffer might print something like:

```plaintext
Output: HELLO WORLD
```
## ✍️ Author’s Note
Honestly, I felt a bit conflicted about uploading this.
While I’m proud of the result and what I’ve learned, I didn’t write it 100% on my own.
But that’s exactly the point of this branch — to show my starting point.
I want to be transparent, and this version helps me see where I began so I can compare it later when I rewrite everything manually.
If you're in the same boat: don’t be ashamed to learn with help. What matters is growing beyond it.
