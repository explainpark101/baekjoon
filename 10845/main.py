from sys import stdin
input = stdin.readline
_stack = []
cmds = {
    "push": _stack.append,
    "pop": lambda: print(_stack.pop(0) if len(_stack) else -1),
    "size": lambda: print(len(_stack)),
    "empty": lambda: print(int(not len(_stack))),
    "front": lambda: print(_stack[0] if len(_stack) else -1),
    "back": lambda: print(_stack[-1] if len(_stack) else -1),
}
for _ in range(int(input())):
    cmd, *args = [_.strip() for _ in input().split(" ")]
    cmds[cmd.strip()](*args)