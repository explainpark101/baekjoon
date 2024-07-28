from sys import stdin
input = stdin.readline
_stack = []
cmds = {
    "push": _stack.append,
    "pop": lambda: print(_stack.pop() if len(_stack) else -1),
    "size": lambda: print(len(_stack)),
    "empty": lambda: print(int(not len(_stack))),
    "top": lambda: print(_stack[-1] if len(_stack) else -1)
}
for _ in range(int(input())):
    cmd, *args = [_.strip() for _ in input().split(" ")]
    cmds[cmd.strip()](*args)