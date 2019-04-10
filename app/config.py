import re

from app.types import Table, Bridge

bridges = Table(
    ao3_search = Bridge(
        match   = lambda url: "archiveofourown.org/works?" in url,
        rootxp  = "//ol[@class = 'work index group']/li",
        idxp    = "dl/dd[@class = 'chapters']/text()",
        titlexp = "div/h4/a/text()",
        urlxp   = "div/h4/a/@href",
        descxp  = ".",
        datexp  = "div/p[@class = 'datetime']/text()",
        datefmt = "%d %b %Y",
    ),
    ao3_work = Bridge(
        match   = lambda url: re.search(
            pattern = re.escape("archiveofourown.org/works/")
                + "[0-9]+"
                + re.escape("/navigate"),
            string = url,
        ),
        reverse = True,
        rootxp  = "//ol[@class = 'chapter index group']/li",
        titlexp = "a/text()",
        urlxp   = "a/@href",
        datexp  = "span[@class = 'datetime']/text()",
        datefmt = "(%Y-%m-%d)",
    ),
)
