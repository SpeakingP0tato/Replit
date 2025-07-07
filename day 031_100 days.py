def colorchange(color):
  if color == "red":
    return("\033[31m")
  elif color == "green":
    return("\033[32m")
  elif color == "yellow":
    return("\033[33m")
  elif color == "blue":
    return("\033[34m")
  elif color == "purple":
    return("\033[35m")
  elif color == "white":
    return("\033[0m")

title = f"{colorchange('red')}={colorchange('white')}={colorchange('blue')}={colorchange('yellow')}Musik App{colorchange('blue')}={colorchange('white')}={colorchange('red')}="

print(f"{title:^35}")
print(f"🔥▶️\t{colorchange('white')}Radio Gaga")
print(f"\t{colorchange('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{colorchange('white')}{prev:<35}")
print(f"{colorchange('green')} {next:^12}")
print(f"{colorchange('purple')}{pause:>15}")

print()
print()
text = "WELCOME TO"
print(f"{colorchange('white')}{text:^13}")
text = "--- ARMBOOK ---"
print(f"{colorchange('blue')}{text:^12}")
text = "Definitely not a rip off"
print(f"{colorchange('yellow')}{text:>12}")
text = "a certain other social"
print(f"{colorchange('yellow')}{text:>12}")
text = "networking site"
print(f"{colorchange('yellow')}{text:>12}")
text = "Honest."
print(f"{colorchange('red')}{text:^12}")
text = "username: "
username = input(f"{colorchange('white')}{text:^12}")
text = "Password: "
password = input(f"{colorchange('white')}{text:^12}")
