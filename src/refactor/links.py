from datetime import date, datetime
from typing import Iterable

from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


def get_html_tags(html: str,
                  html_tag: str | list[str],
                  css_class: str | None = None,
                  bs_method: str = 'html.parser') -> ResultSet[Tag]:

    soup = BeautifulSoup(html, bs_method)
    if css_class:
        return soup.find_all(html_tag, class_=css_class)
    else:
        return soup.find_all(html_tag)


def parse_oil_reports(links: ResultSet[Tag] | Iterable,
                      start_date: date,
                      end_date: date) -> list[tuple]:
    url = "/upload/reports/oil_xls/oil_xls_"
    results = []
    for link in links:
        href = link.get("href")

        if not href:
            continue

        href = href.split("?")[0]
        if url not in href or not href.endswith(".xls"):
            continue

        try:
            date_str = href.split("oil_xls_")[1][:8]
            file = datetime.strptime(date_str, "%Y%m%d").date()
            if start_date <= file <= end_date:
                if href.startswith("http"):
                    u = href
                else:
                    u = f"https://spimex.com{href}"
                results.append((u, file))
            else:
                print(f"Ссылка {href} вне диапазона дат")
        except Exception as e:
            print(f"Не удалось извлечь дату из ссылки {href}: {e}")
    return results
