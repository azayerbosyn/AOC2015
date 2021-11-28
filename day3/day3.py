class Santa:
    x = 0
    y = 0

    def getpos(self):
        return self.x, self.y

    def updatepos(self, i):
        if i == ">":
          self.x += 1
        elif i == "<":
          self.x -= 1
        elif i == "^":
          self.y += 1
        elif i == "v":
          self.y -= 1


def day_3(inp, number_of_santas):

  deliveries = {}
  santas = []
  cnt = 0

  for i in range(0, number_of_santas):
    santas.append(Santa())

  deliveries[0, 0] = number_of_santas

  for i in inp:
    s = cnt % number_of_santas
    santas[s].updatepos(i)
    x, y = santas[s].getpos()
    deliveries[x, y] = 1
    cnt += 1

  return f"{len(deliveries)}"


inp = open("day3_input.txt")
inp = inp.read()
# part1
print(day_3(inp, 1))
# part2 santa+robosanta =2
print(day_3(inp, 2))
