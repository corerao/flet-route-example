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
    # await page.add_async(ft.Row([rail, ft.VerticalDivider(),], expand=True))
    # await page.add_async(ft.Row([ft.Text("Hello, async world!"), ft.VerticalDivider()]))
    # await page.update_async()
    await page.go_async(page.route)


# ft.app_async(main)

if __name__ == "__main__":
    asyncio.run(ft.app_async(target=main))
# import asyncio
# import flet as ft


# async def main(page: ft.Page):
#     async def button_click(e):
#         await asyncio.sleep(1)
#         await page.add_async(ft.Text("Hello!"))

#     await page.add_async(
#         ft.ElevatedButton("Say hello with delay!", on_click=button_click)
#     )

# ft.app(main)
