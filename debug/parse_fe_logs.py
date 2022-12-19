class Stream:
    def __init__(self, iterator):
        self.heads = []
        self.tail = iterator

    def pop_n_into_head(self, n):
        for _ in range(n):
            self.heads.append(next(self.tail))

    def peek_n(self, n):
        deficit = n - len(self.heads)
        self.pop_n_into_head(deficit)
        return self.heads[0:n]

    def peek(self):
        return self.peek_n(1)

    def next_n(self, n):
        next_toks = self.peek_n(n)
        for _ in range(n):
            self.heads.pop(0)
        return next_toks

    def next(self):
        return self.next_n(1)

def parse(s):
    ignore_until_string()

def test_parse(s):
    print(s.peek() == s.peek())
    print(s.peek() == s.next())
    print(s.next != s.next())
    print(s.peek_n(5) == s.next_n(5))
    print(s.peek_n(5))
    print(s.next_n(5))

def main():
    logfilepath = "/Users/noelkwan/projects/risingwave/debug/frontend-4566.log"
    with open(logfilepath, "r") as logs:
        stream = Stream(iter(logs.read()))
        # test_parse(stream)
        parse(stream)

if __name__ == "__main__":
    main()
