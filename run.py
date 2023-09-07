import asyncio

import flet as ft
from flet_route import Routing, path

from views.index_view import IndexView
from views.next_view import NextView


async def main(page: ft.Page):
    page.theme_mode = "DARK"
    page.title = "test"
    app_routes = [
        path(url="/",
             clear=True,
             view=IndexView),
        path(url="/next_view",
             clear=True,
             view=NextView)
    ]
    Routing(page=page,
            app_routes=app_routes, async_is=True)
    await page.go_async(page.route)


if __name__ == "__main__":
    asyncio.run(ft.app_async(target=main))
