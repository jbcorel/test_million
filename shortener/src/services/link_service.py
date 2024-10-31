from datetime import datetime
from src.repos import link_repo
from src.utils.shorten import shorten

def get_short(link: str):
    return link_repo.get_short_link(link)

def get_full(short_link: str):
    return link_repo.get_full_link(short_link)


def create(link: str):
    short_link = shorten(link)
    created_at = str(datetime.now())
    return link_repo.create(
        link=link, short_link=short_link, created_at=created_at
    )


def delete(short_link: str):
    link_repo.delete(short_link=short_link)