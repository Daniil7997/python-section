from dataclasses import dataclass, field
from itertools import batched
from typing import Iterable, TypeAlias

SomeRemoteData: TypeAlias = int


@dataclass
class Query:
    per_page: int = 3
    page: int = 1


@dataclass
class Page:
    per_page: int = 3
    results: Iterable[SomeRemoteData] = field(default_factory=list)
    next: int | None = None


def request(query: Query) -> Page:
    data = [i for i in range(0, 10)]
    chunks = list(batched(data, query.per_page))
    return Page(
        per_page=query.per_page,
        results=chunks[query.page - 1],
        next=query.page + 1 if query.page < len(chunks) else None,
    )


class RetrieveRemoteData:
    def __init__(self, per_page: int = 3, start_page: int = 1):
        self.per_page = per_page
        self.start_page = start_page

    def __iter__(self):
        current_page = self.start_page
        while current_page is not None:
            page_data = request(Query(per_page=self.per_page,
                                      page=current_page))
            if not page_data.results:
                break
            for item in page_data.results:
                yield item
            current_page = page_data.next


class Fibo:
    count = 0
    curr = 1
    prev = 0

    def __init__(self, n: int):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        self.curr, self.prev = self.prev, self.prev + self.curr
        self.count += 1
        return self.curr

    def current(self):
        return self.curr
