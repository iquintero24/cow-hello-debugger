import re

# ✅ Valid Cow language instructions
valid_commands = {
    "moo", "mOo", "moO", "mOO", "Moo", "MOo", "MoO",
    "MOO", "OOO", "MMM", "OOM", "oom"
}

debug_mode = False  # 🔁 True: step-by-step | False: run all at once

# ✅ Clean code: remove comments and invalid characters
def clean_cow_code(content):
    lines = content.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.split(";")[0]  # remove everything after ;
        line = re.sub(r"[^\w\s]", "", line)  # remove special symbols
        cleaned_lines.append(line.strip())

    return " ".join(cleaned_lines)

# ✅ Build jump map for loop handling (MOO ... moo)
def build_jump_map(instructions):
    stack = []
    jump_map = {}
    for i, instr in enumerate(instructions):
        if instr == "MOO":
            stack.append(i)
        elif instr == "moo":
            if not stack:
                raise SyntaxError(f"Error: 'moo' without matching 'MOO' at instruction {i}")
            start = stack.pop()
            jump_map[start] = i
            jump_map[i] = start
    if stack:
        raise SyntaxError("Error: unmatched 'MOO' found")
    return jump_map

# ✅ Optional: Generate Cow code file from a string
def generate_cow_file_from_text(text, filename):
    instructions = []
    for char in text:
        instructions += ["MoO"] * ord(char)
        instructions.append("Moo")
    with open(filename, "w") as f:
        f.write(" ".join(instructions))
    print(f"✅ File '{filename}' generated for text: '{text}'")

# Uncomment to generate a file that prints "Hello World"
# generate_cow_file_from_text("Hello World", "w.cow")

try:
    with open("jdoodle.cow", "r", encoding="utf-8") as file:
        content = file.read()
        cleaned_code = clean_cow_code(content)
        words = cleaned_code.split()
        instructions = [w for w in words if w in valid_commands]

        print(f"\n🎯 Valid instructions loaded ({len(instructions)}):")
        print(instructions)

        memory = [0] * 100
        pointer = 0
        output = ""
        clipboard = None
        ip = 0  # instruction pointer

        jumps = build_jump_map(instructions)

        while ip < len(instructions):
            instr = instructions[ip]

            if debug_mode:
                print(f"\n🔎 Step {ip+1} - Executing: {instr}")
                print(f"📦 Memory: {memory[:10]}")
                print(f"📍 Pointer: {pointer}, Current value: {memory[pointer]}")
                print(f"🖨️ Current output: '{output}'")
                print(f"📋 Clipboard: {clipboard}")
                input("⏸️ Press ENTER to continue...")

            jumped = False

            if instr == "MoO":
                memory[pointer] = (memory[pointer] + 1) % 256
            elif instr == "MOo":
                memory[pointer] = (memory[pointer] - 1) % 256
            elif instr == "moO":
                pointer = (pointer + 1) % len(memory)
            elif instr == "mOo":
                pointer = (pointer - 1) % len(memory)
            elif instr == "Moo":
                if memory[pointer] == 0:
                    user_input = input("⌨️ Input required: ")
                    if user_input:
                        memory[pointer] = ord(user_input[0])
                else:
                    char = chr(memory[pointer])
                    output += char
                    if debug_mode:
                        print(f"✅ Output updated: '{output}' (char: '{char}')")
            elif instr == "MMM":
                if clipboard is None:
                    clipboard = memory[pointer]
                else:
                    memory[pointer] = clipboard
                    clipboard = None
            elif instr == "OOM":
                print(f"🔢 Numeric value: {memory[pointer]}")
            elif instr == "MOO":
                if memory[pointer] == 0:
                    ip = jumps[ip]
                    jumped = True
            elif instr == "moo":
                if memory[pointer] != 0:
                    ip = jumps[ip]
                    jumped = True

            if not jumped:
                ip += 1

        print("\n✅ EXECUTION COMPLETE")
        print(f"🖨️ Final output: '{output}'")

except FileNotFoundError:
    print("❌ File not found: 'w.cow'")
except Exception as e:
    print(f"❌ An error occurred: {e}")
